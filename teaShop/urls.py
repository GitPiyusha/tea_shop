from django.contrib import admin
from django.urls import include, path

from .views import TeaMenuView, TeaOrderView, TeaShopView

urlpatterns = [
    path('shop_list', TeaShopView.as_view(), name='teaShop'),
    path('inventory/<int:tea_shop>/', TeaMenuView.as_view(), name='teaMenu'),
    path('inventory', TeaMenuView.as_view(), name='teaMenu'),
    path('order', TeaOrderView.as_view(), name='teaOrder'),
]