from django.apps import apps
from celery import shared_task
import json
# from django.core.mail import send_mail
# from django.conf import settings

@shared_task
def send_welcome_notification(user_email):
    Notification = apps.get_model('notifications', 'Notification')
    try:
        # Simulate sending welcome email
        print(f"Sending welcome email to {user_email}")
        # In a real app, you'd use:
        # send_mail(
        #     'Welcome to Our App!',
        #     'Thank you for registering!',
        #     'from@example.com',
        #     [user_email],
        #     fail_silently=False,
        # )
        Notification.objects.create(
            email=user_email
        )
        
        return json.dumps({
            "status": "success",
            "email": user_email,
            "type": "welcome",
            "message": "Welcome email sent successfully"
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "email": user_email,
            "type": "welcome",
            "error": str(e)
        })

@shared_task
def send_reminder_notification(user_email):
    Notification = apps.get_model('notifications', 'Notification')
    try:
        # Simulate sending reminder
        print(f"Sending reminder to {user_email}")

        Notification.objects.create(
            email=user_email
        )
        # In a real app, you'd use:
        # send_mail(
        #     'Don\'t forget to complete your profile!',
        #     'Click here to complete your profile setup.',
        #     'from@example.com',
        #     [user_email],
        #     fail_silently=False,
        # )
        
        return json.dumps({
            "status": "success",
            "email": user_email,
            "type": "reminder",
            "message": "Reminder sent successfully"
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "email": user_email,
            "type": "reminder",
            "error": str(e)
        })
