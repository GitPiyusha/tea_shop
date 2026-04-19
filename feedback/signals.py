from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import CustomerFeedbackModel


@receiver(post_save, sender=CustomerFeedbackModel)
def generate_feedback_received_message(sender,instance,created,**kwargs):
    if created:
        print(f"Feedback submitted:{instance.customer_name}, Ratings:{instance.rating},Feedback:{instance.feedback}")