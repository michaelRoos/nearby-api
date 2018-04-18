from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from .models import *
from .serializer import *


class SignupAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = signupSerializer
    queryset = users.objects.all()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    lookup_field = 'pk'
    serializer_class = eventSerializer

    def get_queryset(self):
        qs = event.objects.all();
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = eventSerializer

    def get_queryset(self):
        return event.objects.all();


class TimeAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    lookup_field = 'pk'
    serializer_class = timeSerializer

    def get_queryset(self):
        qs = times.objects.all();
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TimeRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = timeSerializer

    def get_queryset(self):
        return event.objects.all();


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
