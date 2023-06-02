from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from utils import check_project_owner
from utils.decorators import transaction_handler
from ScrumProjects.serializers import ScrumProjectSerializer
from Users.serializers import UserSerializer

from .models import *
from .utils import check_user_in_project, \
check_received_proposal, perfrom_add_member



class ProposalSerializer(serializers.ModelSerializer):
	scrum_project = ScrumProjectSerializer()
	user = UserSerializer()

	class Meta:
		model = Proposal
		fields = '__all__'

	class CreateSerializer(serializers.ModelSerializer):

		def validate(self, attrs):
			if 'scrum_project' in attrs:
				transaction_handler(check_project_owner,
					{'instance': attrs['scrum_project'],
					'scrum': True,
					'user': self.context['request'].user}
				)
				transaction_handler(check_user_in_project,
					{'project':attrs['scrum_project'],
					'user':attrs['user']
					}
				)
				transaction_handler(check_received_proposal,
					{'project':attrs['scrum_project'],
					'user': attrs['user'],
					'scrum': True})
				return super().validate(attrs)
			elif 'kanban_project' in attrs:
				pass 
			else:
				raise ValidationError


		class Meta:
			model = Proposal 
			fields = '__all__'


	class AcceptDeclainSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if not instance.scrum_project:
				project = instance.scrum_project

			return transaction_handler(perfrom_add_member,{
				'project': instance.scrum_project,
				'user': instance.user,
				'role': instance.role,
				'instance':instance
				})

		class Meta:
			model = Proposal
			fields = tuple()