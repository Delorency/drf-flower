from django.db import transaction
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.serializers import IntegerField

from utils.helpers import CreatorForListSerializerHelper, \
CreatorForCreateSerializerHelper, \
CreatorForChangeSerializerHelper
from Tasks.serializers import TaskCardSerializer
from Workspaces.serializers import WorkspaceSerializer
from .utils import create_new_column
from .models import *



class ProjectColumnSerializer(CreatorForListSerializerHelper):

	class Meta:
		model = ProjectColumn
		fields = '__all__'

	class CreateSerializer(CreatorForCreateSerializerHelper):
		project = IntegerField(write_only=True)

		def validate(self, attrs):
			try:
				attrs['creator'] = self.context['request'].user
				attrs['project'] = attrs['creator'].get_user_project(
					attrs['project'])
				return super().validate(attrs) 
			except:
				raise PermissionDenied()

		def create(self, validated_data):
			try:
				with transaction.atomic():
					return create_new_column(validated_data)
			except:
				raise NotFound()

		class Meta:
			model = ProjectColumn
			fields = ('id', 'name', 'number', 'date', 'creator', 'project')

	class UpdateDestroySerializer(CreatorForChangeSerializerHelper):

		class Meta:
			model = ProjectColumn
			fields = ('id', 'name', 'number', 'creator')


class ProjectSerializer(CreatorForListSerializerHelper):
	columns = ProjectColumnSerializer(many=True)
	tasks = TaskCardSerializer(many=True)
	workspace = WorkspaceSerializer()

	class Meta:
		model = Project
		fields = '__all__'

	class CreateSerializer(CreatorForCreateSerializerHelper):

		def validate(self, attrs):
			attrs['creator'] = self.context['request'].user
			if attrs['workspace'].creator != attrs['creator']:  
				raise PermissionDenied()
			return super().validate(attrs) 

		class Meta:
			model = Project
			fields = '__all__'

	class RetrieveUpdateDestroySerializer(CreatorForChangeSerializerHelper):

		class Meta:
			model = Project
			fields = ('id', 'name', 'creator', 'is_private', 'created_at',
				'updated_at')

	class MyListSerializer(CreatorForChangeSerializerHelper):
		columns = ProjectColumnSerializer(many=True)
		tasks = TaskCardSerializer(many=True)
		workspace = WorkspaceSerializer()
		
		class Meta:
			model = Project
			fields = '__all__'