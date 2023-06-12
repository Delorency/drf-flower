from rest_framework import serializers

from djoser.serializers import UserSerializer as dj_UserSerializer

from Users.serializers import UserSerializer
from Members.serializers import MemberSerializer
from utils.decorators import transaction_handler

from .utils import create_new_project

from .models import *



class ScrumProjectSerializer(serializers.ModelSerializer):
	creator = UserSerializer()
	team = MemberSerializer(many=True)

	class Meta:
		model = ScrumProject
		fields = '__all__'


	class CreateSerializer(serializers.ModelSerializer):
		team = MemberSerializer(read_only=True, many=True)
		is_scrum = serializers.BooleanField(default=True)

		def create(self, validated_data):
			return transaction_handler(create_new_project, validated_data)

		class Meta:
			model = ScrumProject
			fields = '__all__'


	class ChangeSerializer(serializers.ModelSerializer):

		class Meta:
			model = ScrumProject 
			fields = ('id', 'name', 'description', 'is_private')