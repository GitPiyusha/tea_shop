from django.contrib import admin
from django.urls import include, path

from .views import CustomerFeedbackView

urlpatterns = [
    path('feedback/list/', CustomerFeedbackView.as_view(), name='customerFeedback'),
    path('feedback/list/<int:shop_id>/', CustomerFeedbackView.as_view(), name='customerFeedbackByShopId'),
    ]

