from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import event
from . serializer import eventSerializer

class eventList(APIView):

	def get(self, request):
		events = event.objects.all()
		serializer = eventSerializer(events, many=True)
		return Response(serializer.data)

	def post(self):
		pass