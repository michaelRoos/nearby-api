
from django.contrib.auth.models import User
import math

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets, status
from .serializer import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time

proximity_weight = 1
popularity_weight = 1
age_weight = 1

class SignupAPIView(generics.ListAPIView, mixins.CreateModelMixin):
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class UpvoteAPIView(generics.ListAPIView, mixins.CreateModelMixin):
	permission_classes = (IsAuthenticated,)
	serializer_class = upvotesSerializer

	def post(self, request, *args, **kwargs):
		if upvotes.objects.filter(user_email=request.data['user_email'],
								  event_id=request.data['event_id']).count() == 0:  # if the user has not upvoted
			# event already
			old_count = event.objects.filter(
				pk=request.data['event_id']).get().upvote_count  # update upvote count for event
			event.objects.filter(pk=request.data['event_id']).update(upvote_count=old_count + 1)
			self.create(request, *args, **kwargs)
			return Response({"is_upvote": True}, status=status.HTTP_202_ACCEPTED)
		else:
			old_count = event.objects.filter(
				pk=request.data['event_id']).get().upvote_count
			event.objects.filter(pk=request.data['event_id']).update(upvote_count=old_count - 1)
			upvotes.objects.filter(user_email=request.data['user_email'],
								  event_id=request.data['event_id']).delete()
			return Response({"is_upvote": False}, status=status.HTTP_202_ACCEPTED)



def event_score(event,age,popularity,proximity,lat,lng,current_time):
	if lat is None or lng is None:
		distance = 0
	else:
		distance = math.sqrt((lat-float(event.lat))**2 + float(lng-event.lng)**2)
	time_dif = event.time_stamp.timestamp() - current_time
	upvotes = event.upvote_count


	distance = distance
	time_dif = time_dif
	upvotes = upvotes

	return age * time_dif + popularity * upvotes + proximity * distance

# 1: a greater
# 0: equal
# -1: b greater


class EventAPIView(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = eventSerializerView


	def get_queryset(self):
		qs = event.objects.all()
		categories_query = self.request.GET.get("categories")
		search_query = self.request.GET.get("search")



		if search_query is not None:
			qs = qs.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
		if categories_query is not None:
			query_split = categories_query.split(',')
			for cat in query_split:
				cat_formated = cat.capitalize()
				qs = qs.filter(categories__title=cat_formated)



		age = self.request.GET.get("age")
		popularity = self.request.GET.get("popularity")
		proximity = self.request.GET.get("proximity")
		lat = self.request.GET.get("lat")
		lng = self.request.GET.get("lng")
		current_time = int(round(time.time() * 1000))

		if(age is None):
			age = age_weight
		if(popularity is None):
			popularity = popularity_weight
		if(proximity is None):
			proximity = proximity_weight

		pk_list = [event.pk for event in sorted(qs, key = lambda e: event_score(e,float(age),popularity,proximity,lat,lng,current_time))]
		clauses = ' '.join(['WHEN mainview_event.id=%s THEN %s' % (pk, i) for i, pk in enumerate(pk_list)])
		ordering = 'CASE %s END' % clauses
		qs = qs.filter(pk__in=pk_list).extra(
			select={'ordering': ordering}, order_by=('ordering',))

		paginator = Paginator(qs, 25)  # Show 25 contacts per page
		qs = paginator.page(1)

		return qs

class EventCreateView(generics.ListAPIView, mixins.CreateModelMixin):
	lookup_field = 'pk'
	serializer_class = eventSerializerCrud
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		qs = event.objects.all()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class EventRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = eventSerializerView

	def get_queryset(self):
		return event.objects.all()

class FileAPIView(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = fileSerializer

	def get_queryset(self):
		qs = file.objects.all()
		return qs

class FileCreateView(generics.ListAPIView, mixins.CreateModelMixin):

	lookup_field = 'pk'
	serializer_class = fileSerializer

	parser_classes = (MultiPartParser, FormParser)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		qs = file.objects.all()
		return qs


	def post(self, request, *args, **kwargs):
		file_serializer = fileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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



class CommentCreateView(generics.ListAPIView, mixins.CreateModelMixin):
	permission_classes = (IsAuthenticated,)
	lookup_field = 'pk'
	serializer_class = commentSerializer

	def get_queryset(self):
		qs = comment.objects.all()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
