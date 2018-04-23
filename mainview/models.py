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


class images(models.Model):
    image_key = models.IntegerField()  # primary key
    img_file = models.BinaryField()
    upload_time = models.DateTimeField()
    user_email = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "images"

    def __str__(self):
        return self.image_key


# class times(models.Model):
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     duration = models.IntegerField()
#     event_id = models.ForeignKey(event, related_name='timeName', on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = "times"
#         unique_together = ("start_time", "end_time", "event_id")
#
#     def __str__(self):
#         return str(self.start_time) + " " + str(self.end_time)





class categories(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


# class event_categories(models.Model):
#     event_id = models.ForeignKey(event, on_delete=models.CASCADE)
#     category = models.ForeignKey(categories, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = "event_categories"
#
#     def __str__(self):
#         return str(self.category) + " " + str(self.event_id)

class event (models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=160)
    location = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10, default=16802)
    user_email = models.CharField(max_length=160)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    comments = JSONField(null=True)
    upvote_count = models.IntegerField(default = 0)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
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