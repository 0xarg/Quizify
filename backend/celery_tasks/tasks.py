import csv
from datetime import timedelta
import os
from celery import shared_task
import time
import pyexcel
import requests
import flask_excel as excel
from models import *
from celery_tasks.mail_service import send_email

# from flask import current_app as app
# celery = app.extensions["celery"]


# @shared_task(ignore_result = True)
# def email_reminder(to,subject, content):
#     send_email(to, subject, content)
    

@shared_task(ignore_results = False, name = "quiz_reminder")
def send_reminders():
    users = User.query.filter(~User.roles.any(Role.name == 'admin')).all()
    for user in users:
        if not user.pref_subjects:
            continue
        
        msg = []
        for subj in user.pref_subjects:
            subject = Subject.query.filter_by(name = subj).first()
            if not subject:
                continue
                
                
            for chapter in subject.chapters:
                for quiz in chapter.quizes:
                    attendance = QuizAttendance.query.filter_by(user_id = user.id, quiz_id = quiz.id).first()
                    if attendance is None:
                        total_ques = quiz.questions.count()
                        chapter_name = chapter.name
                        subject_name = chapter.subject.name
                        remarks = quiz.remarks or "No Remarks."
                        msg.append(
                            f"🔹 *Subject:* {subject_name} |  *Chapter:* {chapter_name} | *Questions:* {total_ques} | *Remarks:* {remarks}")
                       
                            
        if msg:
            content = (
            f"Hi @{user.email.split('@')[0]} 👋\n\n"
            
            f"*New Quizzes Alert for you📝*\n"
            f"{chr(10).join(msg)}\n\n"
            
            f"_You are requested to attempt these quizzes in preparation for the Final Exam._\n"
                f"All the Best!🧠 "
            )
        
            try:
                response = requests.post(
                    "https://chat.googleapis.com/v1/spaces/AAQAy0NuQ3A/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=10L9CFD_Q_m9x17UtOu20lMAyu9Xa7khDs4nMhmC_KU", headers={'Content-type': 'application/json'}, json={"text": content})
                if response.status_code != 200:
                    print(f"Failed to send reminder for quiz {quiz.id} and user{user.email} {response.json()}")
            except Exception as e:
                print(f"Error Sending Reminder to {user.email}: {e}")


@shared_task(ignore_results=False, name="monthly_report")
def monthly_report():
    now = datetime.now()
    first_day = datetime(now.year, now.month, 1)
    last_day = datetime(now.year, now.month + 1,1) - timedelta(days=1)
    users = User.query.filter(~User.roles.any(Role.name == 'admin')).all()
    
    for user in users:
        name = user.email.split('@')[0]
        presents = QuizAttendance.query.filter(QuizAttendance.user_id == user.id, QuizAttendance.visit_time >= first_day, QuizAttendance.visit_time <= last_day).all()
        tQuizes = Quiz.query.filter(Quiz.date >= first_day, Quiz.date <= last_day).count()
        scores = Scores.query.filter(Scores.user_id == user.id, Scores.time >= first_day, Scores.time <= last_day).all()
        table_rows = ""
        for score in scores:
            quiz = score.quiz
            table_rows += f"""
            <tr>
                <td>{quiz.chapter.subject.name}</td>
                <td>{quiz.chapter.name}</td>
                <td>{quiz.date.strftime('%Y-%m-%d')}</td>
                <td>{score.total_score}</td>
                <td>{score.attempts}</td>
            </tr>
            """
        tScores = sum(score.total_score for score in scores)
        avgScore = tScores/len(scores) if scores else 0
        
        
        
        content = f"""
                    <html>
            <head>
                <style>
                    table {{
                        width: 100%;
                        border-collapse: collapse;
                        margin: 20px 0;
                        font-size: 16px;
                        text-align: left;
                    }}
                    th, td {{
                        padding: 12px;
                        border: 1px solid #ddd;
                    }}
                    th {{
                        background-color: #f4f4f4;
                    }}
                </style>
            </head>
            <body>
                <h1>Monthly Activity Report</h1>
                <p>Dear {name},</p>
                <p>Here is your activity report for the month of {now.strftime('%B')}:</p>
                <table>
                    <thead>
                        <tr>
                            <th>Subject</th>
                            <th>Chapter</th>
                            <th>Date</th>
                            <th>Score</th>
                            <th>Attempts</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_rows}
                    </tbody>
                </table>
                <p><strong>Total Quizzes Taken:</strong> {len(scores)}</p>
                <p><strong>Total Score:</strong> {tScores}</p>
                <p><strong>Average Score:</strong> {avgScore:.2f}</p>
                <p>Keep up the great work!</p>
            </body>
            </html>
                    """
            
        try:
            send_email(to=user.email, subject = "Monthly Activity Report", content = content)
            print(f"Monthly Report Sent for {user.email}")
        except Exception as e:
            print(f"Error sending report to user {user.email}: {e}")


@shared_task(ignore_results=False, name="csv_report", bind = True)
def user_quizCsv(self,user_id):
    user = User.query.get(user_id)
    if not user:
        return "User not Found"
    
    scores = Scores.query.filter_by(user_id=user_id).all()
    data = [["Quiz ID", "Chapter", "Date of Quiz", "Score", "Remarks"]]
    for score in scores:
        quiz = score.quiz
        data.append([quiz.id, quiz.chapter.name, quiz.date.strftime('%Y-%m-%d'), score.total_score, quiz.remarks or "No Remarks"])
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"quizReport_{user.email.split('@')[0]}_{now}.csv"
    directory = f"./backend/user_downloads"
    # file_path = os.path.join(directory,filename)
    # pyexcel.save_as(array = data, dest_file_name = file_path)
    
    # if not os.path.exists(directory):
    #     os.makedirs(directory)
        
    with open(f"./backend/user_downloads/{filename}", "w") as file:
        writer = csv.writer(file)
        writer.writerows(data) 
    print(f"File created successfully at: {f"./backend/user_downloads"}")

    
    try:
        mailContent = f"""
            <p>Hi {user.email.split('@')[0]},</p>
            <p>Your quiz details have been exported successfully. Download will be starting soon!.</p>
            <p>Best regards,<br>Quizify Team</p>
            """
        send_email(to=user.email,subject="Quiz report is Ready", content = mailContent)
        print(f"Report ready alert sent to user {user.email}")
    except Exception as e:
        print(f"Error while sending the export done alert: {e}")
        
    return filename
    
    
    
    
    with open(Fpath,"wb") as file:
        wtr = csv.wtr
    
