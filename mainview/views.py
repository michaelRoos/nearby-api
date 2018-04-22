from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets
from .serializer import *

class SignupAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventAPIView(generics.ListAPIView, mixins.CreateModelMixin, viewsets.ViewSet):
    lookup_field = 'pk'
    serializer_class = eventSerializer
    permission_classes_by_action = {'post': [IsAuthenticated],
                                    'default': [AllowAny]}
    def get_queryset(self):
        qs = event.objects.all();
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes_by_action['default']]


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
