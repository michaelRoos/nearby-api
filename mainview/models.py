import datetime

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


class file(models.Model):
  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)
  user_email = models.CharField(max_length=255)

  class Meta:
      verbose_name_plural = "images"


class categories(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class event (models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=160)
    lat = models.CharField(max_length=10)
    long = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=10, default=16802)
    user_email = models.CharField(max_length=160)
    time_stamp = models.DateTimeField(auto_now_add=True)
    comments = JSONField(null=True, blank=True)
    upvote_count = models.IntegerField(default = 0, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    planned_event = models.BooleanField(default=False)
    categories = models.ManyToManyField(categories)
    images = models.ManyToManyField(file, blank=True)

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