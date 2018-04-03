from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class event (models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=160)
	location = models.CharField(max_length=20)
	user_email = models.CharField(max_length=160)
	time = models.DateTimeField()
	comments = JSONField()


	def __str__(self):
		return self.title


# class times (models.Model):
# 	start_time = models.DateTimeField()
# 	end_time = models.DateTimeField()
# 	duration = models.IntegerField()
# 	event_id = models.ForeignKey(event)
#
# 	class Meta:
# 		unique_together = ("start_time", "end_time", "event_id")

