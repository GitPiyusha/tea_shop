from django.db import models

from teaShop.models import TeaMenuModel, TeaShopModel

# Create your models here.
class CustomerFeedbackModel(models.Model):
    shop=models.ForeignKey(TeaShopModel, on_delete=models.CASCADE, related_name='feedback_shop')
    tea=models.ForeignKey(TeaMenuModel, on_delete=models.CASCADE, related_name='feedback_tea')
    customer_name=models.CharField(max_length=100)
    rating=models.FloatField()
    feedback=models.TextField()

    def __str__(self):
        return self.customer_name