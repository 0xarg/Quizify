from celery import shared_task
import time
import requests

import flask_excel
from models import *
# from celery_tasks.emails import send_email
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

