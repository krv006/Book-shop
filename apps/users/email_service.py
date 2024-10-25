from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from users.task import send_activation_email_task


class ActivationEmailService:
    def __init__(self, user, host_url):
        self.user = user
        self.host_url = host_url
        self.token_generator = PasswordResetTokenGenerator()

    def generate_activation_link(self):
        token = self.token_generator.make_token(self.user)
        uid = urlsafe_base64_encode(force_bytes(f"{self.user.pk}/{self.user.is_active}"))
        return f"{self.host_url}/api/v1/users/activate/{uid}/{token}"

    def send_activation_email(self):
        activation_link = self.generate_activation_link()
        from django.template.loader import render_to_string
        from django.utils.html import strip_tags

        subject = 'Registration'
        context = {
            'user': self.user,
            'activation_link': activation_link,
        }
        html_message = render_to_string('email.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <from@example.com>'
        to = self.user.email

        send_activation_email_task.delay(subject, plain_message, [to], html_message=html_message)
