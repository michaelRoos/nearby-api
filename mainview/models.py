import datetime
import uuid

import os
from django.db import models
from django.contrib.postgres.fields import JSONField


# class event(models.Model):
#     title = models.CharField(max_length=20)
#     description = models.CharField(max_length=160)
#     location = models.CharField(max_length=20)
#     user_email = models.CharField(max_length=160)
#     time = models.DateTimeField()
#     comments = JSONField()
#     upvote_count = models.IntegerField(default=0)
#
#     class Meta:
#         verbose_name_plural = "events"
#
#     def __str__(self):
#         return self.title



# class zip_location(models.Model):
#     location = models.CharField(max_length=20)  # primary key
#     zipcode = models.CharField(max_length=10)
#
#     class Meta:
#         verbose_name_plural = "zip_locations"
#
#     def __str__(self):
#         return self.zipcode
from django.template.backends import django

from Nearby.settings.base import MEDIA_ROOT


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(MEDIA_ROOT, filename)


class categories(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

class event (models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=160)
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=10, default=16802)
    user_email = models.CharField(max_length=160)
    time_stamp = models.DateTimeField(auto_now_add=True)
    upvote_count = models.IntegerField(auto_created=0, default=0)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField(categories)

    class Meta:
        verbose_name_plural = "events"

    def __str__(self):
        return self.title

class upvotes(models.Model):
    user_email = models.CharField(max_length=255)
    event_id = models.ForeignKey(event, on_delete=models.CASCADE)
    time = models.DateTimeField()

    class Meta:
        verbose_name_plural = "upvotes"

    def __str__(self):
        return str(self.user_email) + " " + str(self.event_id)

class comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    event_id = models.ForeignKey(event, related_name='event_comment', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "comments"

    def __str__(self):
        return str(self.name) + " : " + str(self.comment)

class file(models.Model):
  file = models.FileField(upload_to=get_file_path, blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)
  user_email = models.CharField(max_length=255)
  event_id = models.ForeignKey(event, related_name='event_images', on_delete=models.CASCADE)

  def __str__(self):
      return str(self.file)

  class Meta:
      verbose_name_plural = "images"

