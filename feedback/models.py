from django.db import models

# Create your models here.
class CustomerFeedbackModel(models.Model):
    shop=models.ForeignKey('teaShop.TeaShopModel', on_delete=models.CASCADE, related_name='feedback_shop')
    tea=models.ForeignKey('teaShop.TeaMenuModel', on_delete=models.CASCADE, related_name='feedback_tea')
    customer_name=models.CharField(max_length=100)
    rating=models.FloatField()
    feedback=models.TextField()

    def __str__(self):
        return self.customer_name