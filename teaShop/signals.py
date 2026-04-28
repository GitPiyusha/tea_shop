import os
import time
from django.dispatch import receiver
from django.db.models.signals import post_save

from services.email_service import EmailServices
from teaShop.tasks import prepare_and_send_email 
from .models import TeaOrderModel


@receiver(post_save, sender=TeaOrderModel)
def generate_invoice(sender, instance, created, **kwargs):
    if created:
        print(f"Invoice generated for order: {instance.id}, Total Price: {instance.total_price}")

        prepare_and_send_email.delay(instance.id)



