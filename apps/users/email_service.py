from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings


class ActivationEmailService:
    def __init__(self, user):
        self.user = user
        self.token_generator = PasswordResetTokenGenerator()

    def generate_activation_link(self):
        token = self.token_generator.make_token(self.user)
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        return f"http://127.0.0.1:8000/activate/{uid}/{token}/"

    def send_activation_email(self):
        activation_link = self.generate_activation_link()
        subject = 'Email tasdiqlash'
        message = f'Hurmatli {self.user.email}, ro‘yxatdan o‘tishni yakunlash uchun quyidagi havolani bosing: {activation_link}'
        recipient_list = [self.user.email]

        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
