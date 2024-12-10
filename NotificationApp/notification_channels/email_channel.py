from django.core.mail import send_mail
from django.conf import settings
from .base import NotificationChannel

class EmailChannel(NotificationChannel):
    def send(self, title: str, content: str, receivers: list) -> bool:
        try:
            send_mail(
                subject=title,
                message=content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=receivers,
                fail_silently=False,
            )
            return True
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False 