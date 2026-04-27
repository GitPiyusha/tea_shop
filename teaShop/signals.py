import os
from django.dispatch import receiver
from django.db.models.signals import post_save

from services.email_service import EmailServices 
from .models import TeaOrderModel


@receiver(post_save, sender=TeaOrderModel)
def generate_invoice(sender, instance, created, **kwargs):
    if created:
        print(f"Invoice generated for order: {instance.id}, Total Price: {instance.total_price}")

        receiver_email = instance.customer_email  
        msg = " Your order has been successfully placed! "

    EmailServices().send_email(
        message=msg,
        sender=os.getenv('EMAIL_ID'),
        recipient=receiver_email
    )