from rest_framework import serializers
from . models import *

class eventSerializer(serializers.ModelSerializer):

	class Meta:
		model = event
		fields = ('title', 'description', 'location', 'time', 'upvote_count')



class timeSerializer(serializers.ModelSerializer):

	class Meta:
		model = times
		fields = ( 'start_time', 'end_time')


class categorySerializer(serializers.ModelSerializer):

	class Meta:
		model = categories
		fields =  ('category')

class upvotesSerializer(serializers.ModelSerializer):

	class Meta:
		model = upvotes
		fields = ('__all__') #hmmm what are we gonna return here cause its not gonna work 


class singleEventSerializer(serializers.ModelSerializer):

	startTime = timeSerializer(many = True, read_only= True)
	#event = eventSerializer(many = True, read_only = True)
	#category = categorySerializer(many = True, read_only = True)

	class Meta:
		model = event
		fields = ('title', 'description', 'location', 'time', 'upvote_count', 'startTime') 


