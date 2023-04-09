from django.db import transaction
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.serializers import IntegerField

from utils.helpers import CreatorForListSerializerHelper, \
CreatorForCreateSerializerHelper, \
CreatorForChangeSerializerHelper
from Users.serializers import UserSerializer
from .utils import create_new_taskcard, create_new_column
from .models import *



class TaskCardSerializer(CreatorForListSerializerHelper):

	class Meta:
		model = TaskCard
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
					return create_new_taskcard(validated_data)
			except:
				raise NotFound()

		class Meta:
			model = TaskCard
			fields = ('id', 'name', 'description', 'creator', 'column', 'project', 'created_at', 
				'updated_at')

	class RetrieveUpdateDestroySerializer(CreatorForChangeSerializerHelper):
		worker = UserSerializer(read_only=True)

		def update(self, instance, validated_data):
			try:
				if 'worker' in validated_data:
					if not validated_data['worker'] in \
						instance.taskcard_projects.all().first().workers.all():
						validated_data.pop('worker')

				return super().update(instance, validated_data)
			except:
				raise PermissionDenied


		class Meta:
			model = TaskCard
			fields = ('id', 'name', 'description', 'worker', 'column', 'creator', 'created_at', 
				'updated_at')