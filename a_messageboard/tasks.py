from django.core.mail import EmailMessage

from celery import shared_task


@shared_task(name="email_notification")
def send_email_task(subject, body, email_addr):
    email = EmailMessage(subject, body, to=[email_addr])
    email.send()
    return email_addr