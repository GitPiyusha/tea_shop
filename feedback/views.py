from urllib import response

from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView, Response
from .models import CustomerFeedbackModel
from .serializer import FeedbackSerializer

# Create your views here.

class CustomerFeedbackView(APIView):
    serializer_class=FeedbackSerializer

    def get(self,request):
        feedbacks=CustomerFeedbackModel.objects.all()
        serializer=FeedbackSerializer(feedbacks,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
