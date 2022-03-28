import time
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task(email):
    """background task to send an email asynchronously"""
    subject = 'Helo from Celery'
    message = 'This is a test email sent asynchronously with Celery.'

    time.sleep(5)
    return send_mail(
        subject,
        message,
        'sarwardevcs@gmail.com',
        [email],
        fail_silently=False
    )


@shared_task
def add(x, y):
    return x + y
