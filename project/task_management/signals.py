from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .tasks import send_task_notification_email

@receiver(post_save, sender=Task)
def send_task_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Task Created'
        message = f'Task "{instance.title}" has been created successfully.'
    else:
        subject = 'Task Updated'
        message = f'Task "{instance.title}" has been updated successfully.'

    # Enviar correo de manera asíncrona usando Celery
    send_task_notification_email.delay(subject, message, instance.email)
