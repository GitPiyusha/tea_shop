from urllib import request, response

from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView, Response
from teaShop.models import TeaMenuModel, TeaShopModel
from teaShop.serializer import MenuSerializer, OrderSerializer, ShopSerializer



# Create your views here.

class TeaShopView(APIView):

    serializer_class=ShopSerializer

    def get(self,request):
        teas_shop=TeaShopModel.objects.all()
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

    def get(self,request):
        tea_menu=TeaMenuModel.objects.all()
        serializer=MenuSerializer(tea_menu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
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
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)