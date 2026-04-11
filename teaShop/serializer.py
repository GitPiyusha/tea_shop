from rest_framework import serializers

from teaShop.models import TeaMenuModel, TeaOrderModel, TeaShopModel


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeaShopModel
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    available_quantity=serializers.IntegerField()
    price_per_cup=serializers.FloatField()

    class Meta:
        model=TeaMenuModel
        fields='__all__'

    def validate_available_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Available quantity cannot be negative.")
        return value

    def validate_price_per_cup(self, value):
        if value < 0:
            raise serializers.ValidationError("Price per cup cannot be negative.")
        return value

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeaOrderModel
        fields='__all__'
        