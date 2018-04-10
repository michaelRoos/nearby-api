from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializer import *


class timesList(APIView):

	def get(self, request):
		time = times.objects.all()
		serializer = timeSerializer(time, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class eventList(APIView):

	def get(self, request):
		events = event.objects.all()
		serializer = eventSerializer(events, many=True)
		return Response(serializer.data)

	def post(self):
		pass


class categoryList(APIView):

	def get(self, request):
		category = categories.objects.all()
		serializer = categorySerializer(category, many=True)
		return Response(serializer.data)

	def post(self):
		pass



class upvotesList(APIView):

	def get(self, request):
		upvote = upvotes.objects.all()
		serializer = upvotesSerializer(upvote, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class singleEventList(APIView):

	def get(self, request):
		singleEvents = event.objects.all()
		serializer = singleEventSerializer(singleEvents, many=True)
		return Response(serializer.data)

	def post(self):
		pass








