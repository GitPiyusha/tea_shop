from rest_framework import serializers

from teaShop.models import TeaMenuModel, TeaOrderModel, TeaShopModel


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeaShopModel
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeaMenuModel
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeaOrderModel
        fields='__all__'
        