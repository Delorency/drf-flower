from django.db import transaction

from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from djoser.serializers import UserSerializer as dj_UserSerializer

from Users.serializers import UserSerializer
from Members.serializers import MemberSerializer

from .models import *



class ScrumProjectSerializer(serializers.ModelSerializer):
	creator = UserSerializer()
	team = MemberSerializer(many=True)

	class Meta:
		model = ScrumProject
		fields = '__all__'


	class CreateSerializer(serializers.ModelSerializer):
		creator = dj_UserSerializer(read_only=True)
		team = MemberSerializer(read_only=True, many=True)

		def validate(self, attrs):
			attrs['creator'] = self.context['request'].user
			return super().validate(attrs) 

		def create(self, validated_data):
			try:
				with transaction.atomic():
					return create_new_project(validated_data)
			except:
				raise ValidationError()

		class Meta:
			model = ScrumProject
			fields = '__all__'


	class RetrieveUpdateDestroySerializer(serializers.ModelSerializer):
		creator = dj_UserSerializer(read_only=True)

		def update(self, instance, validated_data):
			pass

		class Meta:
			model = ScrumProject 
			fields = '__all__'