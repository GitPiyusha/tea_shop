from urllib import request, response

from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status
from rest_framework.views import APIView, Response
from teaShop.models import TeaMenuModel, TeaOrderModel, TeaShopModel
from teaShop.serializer import MenuSerializer, OrderSerializer, ShopSerializer



# Create your views here.

class TeaShopView(APIView):

    serializer_class=ShopSerializer

    def get(self,request):
        teas_shop=TeaShopModel.objects.all().order_by('-rating')
        serializer=ShopSerializer(teas_shop,many=True)
        return Response(serializer.data,status=200)

    def post(self,request):

        serializer= ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def put(self, request, id=None):
        try:
            tea_shop = TeaShopModel.objects.get(id=id)
        except TeaShopModel.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        serializer = ShopSerializer(tea_shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

class TeaMenuView(APIView):
    serializer_class=MenuSerializer

    def get(self,request,tea_shop):
            tea_menu=TeaMenuModel.objects.filter(tea_shop_id=tea_shop)
            serializer=MenuSerializer(tea_menu,many=True)
            return Response(serializer.data, status=200)
    
    def get(self,request):
            tea_menu=TeaMenuModel.objects.all()
            serializer=MenuSerializer(tea_menu,many=True)
            return Response(serializer.data, status=200)
    
    def post(self,request):
        serializer=MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class TeaOrderView(APIView):
    serializer_class=OrderSerializer

    def post(self,request):
        tea_id= request.data.get('tea')
        quantity=int( request.data.get('quantity'))

        try:
            tea_menu=TeaMenuModel.objects.get(id=tea_id)
        except TeaMenuModel.DoesNotExist:
            return Response({"error": "Tea not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if tea_menu.available_quantity < quantity:
            return Response({"error": "Insufficient quantity"}, status=status.HTTP_400_BAD_REQUEST)
        

        tea_menu.available_quantity-=quantity
        tea_menu.save()

        order= TeaOrderModel.objects.create(tea=tea_menu,quantity=quantity,order_status='pending',customer_email=request.data.get('customer_email'))

        return Response({ "total_price": order.total_price, "order_id": order.id,"quantity": order.quantity,"tea_id": order.tea.id,"order_status": order.order_status}, status=status.HTTP_201_CREATED)
    

    def get(self,request):
        orders=TeaOrderModel.objects.all()
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data, status=200)