from rest_framework import serializers
from djoser.serializers import UserSerializer as dj_UserSerializer

from Users.serializers import UserSerializer
from .models import *



class WorkspaceSerializer(serializers.ModelSerializer):

	creator = UserSerializer()

	class Meta:
		model = Workspace
		fields = ('id', 'name', 'creator', 'is_private', 'created_at')

	class CreateSerializer(serializers.ModelSerializer):

		creator = UserSerializer(read_only=True)

		def create(self, validated_data):
			validated_data['creator'] = self.context['request'].user
			return super().create(validated_data)

		class Meta:
			model = Workspace
			fields = '__all__'
	
	class RetrieveUpdateDestroySerializer(serializers.ModelSerializer):
		creator = dj_UserSerializer(read_only=True)

		class Meta:
			model = Workspace
			fields = '__all__'