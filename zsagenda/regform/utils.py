
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_registration_email(registration_answer):
    msg_plain = render_to_string(
        'mail/registration_confirmation.txt',
        dict(
            reg_obj=registration_answer,
        )
    )
    email = EmailMessage(
        subject='Potvrzení o registraci k zápisu',
        body=msg_plain,
        from_email=settings.REG_FORM_EMAIL_SENDER,
        to=[
            registration_answer.email,
        ],
        cc=settings.REG_FORM_EMAIL_CC,
    )
    email.send()
    registration_answer.email_sent = True
    registration_answer.save()
