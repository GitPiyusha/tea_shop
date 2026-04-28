import time
from celery import shared_task

from services.email_service import EmailServices
from teaShop.models import TeaOrderModel

@shared_task
def prepare_and_send_email(order_id):
    order = TeaOrderModel.objects.get(id=order_id)

    receiver_email = order.customer_email  
    msg = " Your order has been successfully placed! "
    time.sleep(15)  # Simulating delay in sending email
    order.order_status = 'completed'
    order.save()
        
    EmailServices().send_email(
        message=msg,
        recipient=receiver_email
    )