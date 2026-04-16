from django.dispatch import receiver
from django.db.models.signals import post_save

from teaShop.models import TeaOrderModel

@receiver(post_save, sender=TeaOrderModel)
def generate_invoice(sender, instance, created, **kwargs):
    if created:
        print(f"Invoice generated for order: {instance.id}, Total Price: {instance.total_price}")