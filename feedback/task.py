

import time

from celery import shared_task

from feedback.models import CustomerFeedbackModel
from services.email_service import EmailServices

@shared_task
def send_feedback(feedback_id):
    feedback=CustomerFeedbackModel.objects.get(id=feedback_id)

    receiver_email = feedback.customer_email 
    msg="Thanks for your feedback"

    time.sleep(5)

    EmailServices().send_email(
        message=msg,
        recipient=receiver_email
    )

