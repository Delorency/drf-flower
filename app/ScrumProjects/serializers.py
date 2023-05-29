from django.db import transaction

from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from djoser.serializers import UserSerializer as dj_UserSerializer

from Users.serializers import UserSerializer
from Members.serializers import MemberSerializer
from .utils import create_new_project

from .models import *



class ScrumProjectSerializer(serializers.ModelSerializer):
	creator = UserSerializer()
	team = MemberSerializer(many=True)

	class Meta:
		model = ScrumProject
		fields = '__all__'


	class CreateSerializer(serializers.ModelSerializer):
		is_scrum = serializers.BooleanField(read_only=True)
		team = MemberSerializer(read_only=True, many=True)

		def create(self, validated_data):
			try:
				with transaction.atomic():
					return create_new_project(validated_data)
			except:
				raise ValidationError()

		class Meta:
			model = ScrumProject
			fields = '__all__'


	class ChangeSerializer(serializers.ModelSerializer):

		class Meta:
			model = ScrumProject 
			fields = ('id', 'name', 'description', 'is_private')