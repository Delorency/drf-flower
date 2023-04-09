from django.db import transaction
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.serializers import IntegerField

from utils.helpers import CreatorForListSerializerHelper, \
CreatorForCreateSerializerHelper, \
CreatorForChangeSerializerHelper
from djoser.serializers import UserSerializer
from Users.serializers import UserSerializer as MyUserSerializer
from Tasks.serializers import TaskCardSerializer
from Workspaces.serializers import WorkspaceSerializer
from .models import *



class ProjectSerializer(CreatorForListSerializerHelper):
	tasks = TaskCardSerializer(many=True)
	workspace = WorkspaceSerializer()

	class Meta:
		model = Project
		fields = ('id', 'name', 'creator', 'tasks', 'workspace', 
			'is_private', 'created_at', 'updated_at')

	class CreateSerializer(CreatorForCreateSerializerHelper):

		def validate(self, attrs):
			attrs['creator'] = self.context['request'].user
			if not attrs['workspace'].check_creator(attrs['creator']):  
				raise PermissionDenied()
			return super().validate(attrs) 

		class Meta:
			model = Project
			fields = ('id', 'name', 'creator', 'workspace', 
			'is_private', 'created_at', 'updated_at')

	class RetrieveUpdateDestroySerializer(CreatorForChangeSerializerHelper):

		class Meta:
			model = Project
			fields = ('id', 'name', 'creator', 'is_private', 'created_at',
				'updated_at')

	class MyListSerializer(CreatorForChangeSerializerHelper):
		tasks = TaskCardSerializer(many=True)
		workers = MyUserSerializer(many=True)
		workspace = WorkspaceSerializer()
		
		class Meta:
			model = Project
			fields = '__all__'



class ProposalSerializer(CreatorForListSerializerHelper):
	project = ProjectSerializer()
	user = UserSerializer()

	class Meta:
		model = Proposal
		fields = ('id', 'user', 'project', 'message', 'creator','created_at',
			'updated_at')

	class CreateSerializer(CreatorForCreateSerializerHelper):

		def validate(self, attrs):
			attrs['creator'] = self.context['request'].user
			if not attrs['project'].check_creator(attrs['creator']):  
				raise PermissionDenied()
			return super().validate(attrs) 

		class Meta:
			model = Proposal
			fields = ('id', 'user', 'project', 'message', 'creator',
				'created_at', 'updated_at')