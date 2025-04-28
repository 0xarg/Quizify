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
def send_reminders(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    # print(quiz)

    if not quiz:
        print(f"No quiz found with id {quiz_id}")
        return

    users = User.query.filter(~User.roles.any(Role.name == 'admin'), ~User.id.in_(db.session.query(QuizAttendance.user_id).filter(QuizAttendance.quiz_id == quiz_id))).all()
    chapter_name = quiz.chapter.name if quiz.chapter else "Unknown Chapter."
    total_ques = quiz.questions.count()
    url = "https://chat.googleapis.com/v1/spaces/AAQAy0NuQ3A/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=10L9CFD_Q_m9x17UtOu20lMAyu9Xa7khDs4nMhmC_KU"
    # try:
    #     response = requests.post(
    #         url,
    #         headers={'Content-Type': 'application/json'},
    #         json=message,
    #         timeout=10   # Always set a timeout!
    #     )
    #     print(f"Status Code: {response.status_code}")
    #     print(f"Response Text: {response.text}")


    # except requests.exceptions.RequestException as e:
    #     print(f"Error occurred: {e}")
        
    
    subject = f"New Quiz Available"
   
    # text = "Radha Vallabh Shri Harivansh"
    for user in users:
        content = f"""
        For @{user.email.split('@')[0]}
        *New Quiz Added!!*\n
        *Chapter:* {chapter_name}\n
        *Total Questions:* {total_ques}\n
        *Remarks:* {quiz.remarks or "No Remarks."}\n
        _Learners are requested to attempt this quiz in order to get prepared for the Final Exam._\n
        All the Best!
        """
        response = requests.post(
            "https://chat.googleapis.com/v1/spaces/AAQAy0NuQ3A/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=10L9CFD_Q_m9x17UtOu20lMAyu9Xa7khDs4nMhmC_KU", headers={'Content-type': 'application/json'}, json={"text": content})
        # send_email(to=user.email, subject=subject, content=content)
    print(f"Reminder sent to {len(users)} users for the new Quiz.")
