from django.shortcuts import render
from rest_framework.views import APIView
from .models import Sponsorship, Contact
from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from .serializers import ContactSerializer, SponsorshipSerializer

# Create your views here.
class ContactView(APIView):
    def post(self, request, format=None):
            data = request.data
            serializer = ContactSerializer(data = data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'msg': 'Your message has been sent. The Advaita Mail Man is on the way :)'
                },  status=status.HTTP_200_OK)
            return Response({
                'msg': serializer.errors
            }, status=status.HTTP_404_NOT_FOUND)

class SponsorshipContactView(APIView):
    def post(self, request, format=None):
            data = request.data
            serializer = SponsorshipSerializer(data = data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'msg': 'Thank you for contacting us. We`ve received your message and will get back to you supersoon'
                },  status=status.HTTP_200_OK)
            return Response({
                'msg': serializer.errors
            }, status=status.HTTP_404_NOT_FOUND)
