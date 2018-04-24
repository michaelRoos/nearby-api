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
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'event/create', EventCreateView.as_view(), name="event-create-and-list"),
    url(r'event/list', EventAPIView.as_view(), name="event-create-and-list"),
    url(r'event/(?P<pk>\d+)/', EventRudView.as_view(), name="event-rud"),
    url(r'signup', SignupAPIView.as_view(), name="signup"),
    url(r'^api-token-auth', obtain_jwt_token),
    url(r'upvote', UpvoteAPIView.as_view(), name="upvote"),
    url(r'^image/upload$', FileCreateView.as_view(), name='file-upload'),
    url(r'^image/list', FileAPIView.as_view(), name='file-upload'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
