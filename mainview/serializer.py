from django.contrib.auth import get_user_model
from rest_framework import serializers

from Nearby.settings.base import MEDIA_ROOT
from .models import *
import datetime


class eventSerializer(serializers.ModelSerializer):
	class Meta:
		model = event
		fields = '__all__'


class commentSerializer(serializers.ModelSerializer):
	class Meta:
		model = comment
		fields = ('__all__')


class fileSerializer(serializers.ModelSerializer):
	class Meta():
		model = file
		fields = ('__all__')

	def to_representation(self, obj):
		return {
			'id': obj.id,
			'file': os.environ.get("MEDIA_URL") + obj.file,
			'timestamp': obj.timestamp,
			'user_email': obj.user_email,
			'event_id': str(obj.event_id)
		}

	def create(self, validated_data):
		image = file.objects.create(
			user_email=validated_data['user_email'],
			file=validated_data['file'],
			timestamp=datetime.datetime.now(),
			event_id = validated_data['event_id'])
		image.save()
		return image

class categorySerializer(serializers.ModelSerializer):
	class Meta:
		model = categories
		fields = ('title',)

class upvotesSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		upvote = upvotes.objects.create(
			user_email=validated_data['user_email'],
			event_id=validated_data['event_id'],
			time=datetime.datetime.now())
		upvote.save()
		return upvote

	class Meta:
		model = upvotes
		fields = ('user_email', 'event_id')


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	def create(self, validated_data):
		user = UserModel.objects.create(
			username=validated_data['email']
		)
		user.set_password(validated_data['password'])
		user.save()

		return user

	class Meta:
		model = UserModel
		fields = ('email', 'password')


class eventSerializerView(serializers.ModelSerializer):

	categories = categorySerializer(many=True)
	event_images = fileSerializer(read_only=True, many=True)
	event_comment = commentSerializer(read_only=True, many=True)

	class Meta:
		model = event
		fields = ('id','title', 'description', 'event_images', 'event_comment', 'lat', 'lng', 'zipcode', 'time_stamp', 'upvote_count' , 'start_time', 'end_time', 'user_email', 'categories')




class eventSerializerCrud(serializers.ModelSerializer):

	categories = serializers.SlugRelatedField(many=True, queryset=categories.objects, slug_field="title")


	def create(self, validated_data):
		validated_data_no_cat = validated_data.copy()
		validated_data_no_cat.pop('categories')
		m_event = event.objects.create(**validated_data_no_cat)
		for category_title in validated_data['categories']:
			category = categories.objects.filter(title=category_title).first()
			while category is not None:
				m_event.categories.add(category)
				if category is category.parent:
					category = None
				else:
					category = category.parent
		m_event.save()
		return m_event

	class Meta:
		model = event
		fields = ('id','title', 'description','lat', 'lng', 'zipcode', 'time_stamp', 'upvote_count' , 'start_time', 'end_time', 'user_email', 'categories')
