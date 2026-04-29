import os

from django.dispatch import receiver
from django.db.models.signals import post_save

from feedback.task import send_feedback
from services.email_service import EmailServices 

from .models import CustomerFeedbackModel


@receiver(post_save, sender=CustomerFeedbackModel)
def generate_feedback_received_message(sender,instance,created,**kwargs):
    if created:
        print(f"Feedback submitted:{instance.customer_name}, Ratings:{instance.rating},Feedback:{instance.feedback}")

    #     receiver_email=instance.customer_email
    #     msg="Thanks for your valuable feedback. "

    # EmailServices().send_email( message=msg,
    #                            sender=os.getenv('EMAIL_ID'),
    #                            recipient=receiver_email)

    send_feedback.delay(instance.id)