from django.contrib.auth.models import User
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
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			return Response(status=status.HTTP_403_FORBIDDEN)


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
			pass
		return qs

class EventSingleView(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = eventSerializerView

	def get_queryset(self):
		qs = event.objects.all()
		pk = self.kwargs['pk']
		if pk is not None:
			qs = qs.filter(pk=pk)
		return qs

class EventCreateView(generics.ListAPIView, mixins.CreateModelMixin):
	lookup_field = 'pk'
	serializer_class = eventSerializerCrud
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		qs = event.objects.all()
		categories_query = self.request.GET.get("categories")
		search_query = self.request.GET.get("search")
		if search_query is not None:
			qs = qs.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
		if categories_query is not None:
			temp = 2
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
	# permission_classes = (IsAuthenticated,)

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
	# permission_classes = (IsAuthenticated,)
	lookup_field = 'pk'
	serializer_class = commentSerializer

	def get_queryset(self):
		qs = comment.objects.all()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
