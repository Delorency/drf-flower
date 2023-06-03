from rest_framework import serializers

from utils import check_project_owner
from utils.decorators import transaction_handler
from Backlogs.serializers import BacklogSerializer
from ScrumProjects.serializers import ScrumProject

from .models import *
from .utils import get_valid_backlogs



class SprintSerializer(serializers.ModelSerializer):
	backlogs = BacklogSerializer(many=True)
	scrum_project = ScrumProject()

	class Meta:
		model = Sprint 
		fields = '__all__'


	class CreateSerializer(serializers.ModelSerializer):

		def validate(self, attrs):
			transaction_handler(check_project_owner,
				{'instance':attrs['scrum_project'],
				'user':self.context['request'].user,
				'scrum':True}
				)
			return super().validate(attrs)

		class Meta:
			model = Sprint 
			fields = ('id', 'start_at', 'end_at', 'scrum_project')


	class UpdateSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if 'backlogs' in validated_data:
				validated_data['backlogs'] = \
				transaction_handler(get_valid_backlogs, 
					{'instance': instance,
					'backlogs':validated_data.get('backlogs')})
			return super().update(instance, validated_data)

		class Meta:
			model = Sprint 
			fields = ('backlogs',)