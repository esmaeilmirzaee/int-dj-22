from django.conf import settings
from django.core.mail import send_mail


def send_email(subject, to, message, full_name):
    from_email = settings.EMAIL_HOST_USER
    to_email = to
    send_mail(subject, message, from_email, to_email)
