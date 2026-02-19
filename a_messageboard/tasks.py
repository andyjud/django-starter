from datetime import datetime

from django.core.mail import EmailMessage

from celery import shared_task
from django.template.loader import render_to_string


@shared_task(name="email_notification")
def send_email_task(subject, body, email_addr, is_html=False):
    email = EmailMessage(subject, body, to=[email_addr])
    if is_html:
        email.content_subtype = "html"
    email.send()
    return f"Mail to: {email_addr}"


@shared_task(name="monthly_newsletter")
def send_newsletter_task():
    from a_messageboard.models import MessageBoard
    subject = "Your Monthly Newsletter 🗞"
    subscriber = MessageBoard.objects.get(id=1).subscribers.last()
    context = {"name": subscriber.profile.name}
    body = render_to_string("message_board/newsletter.html", context)
    send_email_task(subject, body, subscriber.email, True)

    current_month = datetime.now().strftime("%B")
    return f"{current_month} Newsletter Sent: {subscriber.email}"

