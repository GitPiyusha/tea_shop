from django.db import models

# Create your models here.
class TeaShopModel(models.Model):
    name=models.CharField(max_length=20)
    location=models.TextField()
    rating=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class TeaMenuModel(models.Model):
    tea_shop=models.ForeignKey(TeaShopModel,on_delete=models.CASCADE,related_name='tea_shop')
    flavour=models.CharField(max_length=20)
    available_quantity=models.PositiveIntegerField()
    price_per_cup=models.FloatField()

    def __str__(self):
         if self.flavour:
             return self.flavour + " - " + self.tea_shop.name


class TeaOrderModel(models.Model):
    tea=models.ForeignKey(TeaMenuModel,on_delete=models.CASCADE,related_name='tea_orders')
    quantity=models.IntegerField()
    total_price=models.FloatField(blank=True, null=True)
    ordered_at=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(choices=[('pending','pending'),('completed','completed')],default='pending')

    def save(self, *args, **kwargs):
        self.total_price=self.quantity*self.tea.price_per_cup
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tea.name