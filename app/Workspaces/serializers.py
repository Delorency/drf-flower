from rest_framework import serializers
from djoser.serializers import UserSerializer as djoser_UserSerializer

from Users.serializers import UserSerializer

from utils.helpers import CreatorSerializerHelper
from .models import *



class WorkspaceSerializer(serializers.ModelSerializer):

	creator = UserSerializer()

	class Meta:
		model = Workspace
		fields = ('id', 'name', 'creator', 'is_private', 'created_at')

	class CreateSerializer(CreatorSerializerHelper):

		class Meta:
			model = Workspace
			fields = '__all__'
	
	class RetrieveUpdateDestroySerializer(serializers.ModelSerializer):
		creator = djoser_UserSerializer(read_only=True)

		class Meta:
			model = Workspace
			fields = '__all__'