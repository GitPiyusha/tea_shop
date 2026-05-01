import random
import time
from celery import shared_task

from services.email_service import EmailServices
from teaShop.models import TeaOrderModel

@shared_task
def prepare_and_send_email(order_id):
    order = TeaOrderModel.objects.get(id=order_id)
    tea = order.tea

    receiver_email = order.customer_email  
    decision = random.randint(0, 1)
    print("Decision: ", decision)
    time.sleep(15)  # Simulating delay in sending email
    if decision == 1:
        order.order_status = 'completed'
        subject = "Order Confirmation"
        print(subject)
        msg = " Your order has been successfully placed! "
    else:
        order.order_status = 'cancelled'
        tea.available_quantity += order.quantity
        subject = "Order Update"
        print(subject)
        msg = " Unfortunately, your order could not be processed. Please try again later. "
        tea.save()
    order.save()
        
    EmailServices().send_email(
        subject=subject,
        message=msg,
        recipient=receiver_email
    )