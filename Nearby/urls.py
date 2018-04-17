"""Nearby URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mainview.views import *




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'event/list', EventAPIView.as_view(), name="event-create-and-list"),
    url(r'event/(?P<pk>\d+)/', EventRudView.as_view(), name="event-rud"),
    url(r'times/list', TimeAPIView.as_view(), name="event-create-and-list"),
    url(r'times/(?P<pk>\d+)/', TimeRudView.as_view(), name="event-rud"),


    # url(r'^events/single/', views.singleEventList.as_view()),
    # url(r'^events/', views.eventList.as_view()),
    # url(r'^times/', views.timesList.as_view()),
    # url(r'^category/', views.categoryList.as_view()),
    # url(r'^upvotes/', views.upvotesList.as_view()),



]
