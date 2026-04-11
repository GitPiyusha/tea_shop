from django.contrib import admin
from django.urls import include, path

from .views import CustomerFeedbackView

urlpatterns = [
    path('feedback_list', CustomerFeedbackView.as_view(), name='customerFeedback'),
    ]