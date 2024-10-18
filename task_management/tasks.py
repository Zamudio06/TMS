from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_task_notification_email(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        'zamudiod13@gmail.com',
        [recipient_email],
        fail_silently=False,
    )
