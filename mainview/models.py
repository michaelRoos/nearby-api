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
	upvote_count = models.IntegerField(default = 0)


	def __str__(self):
		return self.title


class users (models.Model):
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 25)

	def __str__(self):
		return self.email

class zip_location (models.Model):
	location = models.CharField(max_length = 20) #primary key
	zipcode = models.CharField(max_length = 10)	

	def __str__(self):
		return self.zipcode

class images (models.Model):
	image_key = models.IntegerField() #primary key
	img_file = models.BinaryField()	
	upload_time = models.DateTimeField()	
	user_email = models.CharField(max_length = 255)	

	def __str__(self):
		return self.image_key


class times (models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	duration = models.IntegerField()
	event_id = models.ForeignKey(event, related_name = 'timeName', on_delete = models.CASCADE)


	class Meta:
 		unique_together = ("start_time", "end_time", "event_id")

class upvotes (models.Model):
        user_email = models.CharField(max_length = 255)
        event_id = models.ForeignKey(event, on_delete = models.CASCADE)
        time = models.DateTimeField()
        
class categories (models.Model):
        name = models.CharField(max_length = 255)
        parent = models.ForeignKey(event, on_delete = models.CASCADE)

class event_categories (models.Model):
        event_id = models.ForeignKey(event, on_delete = models.CASCADE)
        category = models.ForeignKey(categories, on_delete = models.CASCADE)








