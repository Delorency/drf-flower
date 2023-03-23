from django.db import transaction, IntegrityError
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.serializers import IntegerField

from utils.helpers import CreatorForListSerializerHelper, \
CreatorForCreateSerializerHelper, \
CreatorForChangeSerializerHelper
from Users.serializers import UserSerializer
from .utils import create_new_column
from .models import *



class ProjectSerializer(CreatorForListSerializerHelper):

	class Meta:
		model = Project
		fields = ('id', 'name', 'creator', 'is_private',
			'created_at')

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


class ProjectColumnSerializer(CreatorForListSerializerHelper):

	class Meta:
		model = ProjectColumn
		fields = ('id', 'name', 'creator', 'created_at')

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
			fields = ('id', 'name', 'number', 'creator', 'project')

	class UpdateDestroySerializer(CreatorForChangeSerializerHelper):
		project = ProjectSerializer(read_only=True)

		class Meta:
			model = ProjectColumn
			fields = ('id', 'name', 'number', 'creator', 'project')