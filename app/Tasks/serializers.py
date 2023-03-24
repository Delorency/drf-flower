from django.db import transaction
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.serializers import IntegerField

from utils.helpers import CreatorForListSerializerHelper, \
CreatorForCreateSerializerHelper, \
CreatorForChangeSerializerHelper
from .utils import create_new_taskcard
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
			fields = '__all__'

	class RetrieveUpdateDestroySerializer(CreatorForChangeSerializerHelper):

		class Meta:
			model = TaskCard
			fields = '__all__'