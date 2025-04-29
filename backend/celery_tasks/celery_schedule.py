from celery.schedules import crontab
from celery_tasks.tasks import send_reminders
from flask import current_app as app
celery_app = app.extensions["celery"]


@celery_app.on_after_configure.connect  # --> basically lifecycle like vue
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=12, minute=3),
        send_reminders.s(),
        name="Daily Quiz Reminder"
    )
    # sender.add_periodic_task(
    #     10.0,
    #     send_reminders.s(),
    #     name="Daily Quiz Reminder"
    # )
    # sender.add_periodic_task(
    #     10.0,
    #     test.s("testing 1234"),
    #     name="Test Reminder"
    # )

#     # --> Every 10 seconds
#     # sender.add_periodic_task(10.0, email_reminder.s('Student@project','reminder tp login', '<h1>Hello to everyone 😁</h1>'))

    # --> Every day at 15:48
    #    sender.add_periodic_task(crontab(hour=15,minute=48), email_reminder.s('Student@project','reminder to login', '<h1>Hello to everyone 😁</h1>'))

#     # Weekly Reminder
#     sender.add_periodic_task(crontab(hour=15, minute=51),send_reminders.s(quiz_id))

# @celery_app.task
# def test(arg):
#     print(arg)
