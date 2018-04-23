from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
import datetime


class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = '__all__'


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
        fields = ('user_email', 'event_id')  # hmmm what are we gonna return here cause its not gonna work


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
    # user = UserSerializer()
    categories = categorySerializer(many=True)

    class Meta:
        model = event
        # fields = ('id','title', 'description', 'location', 'zipcode', 'time_stamp', 'comments', 'upvote_count' , 'start_time', 'end_time', 'user', 'categories')
        fields = ('__all__')


class eventSerializerCrud(serializers.ModelSerializer):

    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")

    def create(self, validated_data):
        m_event = event.objects.create(
            title=validated_data["title"],
            location=validated_data["location"],
            description=validated_data["description"],
            user_email=validated_data["user_email"]
        )
        category = validated_data['categories']
        while category is not None:
            m_event.categories.add(category.parent)
            category = category.parent
        m_event.save()

        return m_event

    class Meta:
        model = event
        fields = (
        'id', 'title', 'description', 'location', 'zipcode', 'time_stamp', 'comments', 'upvote_count', 'start_time',
        'end_time', 'user_email', 'categories')
