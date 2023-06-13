from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from utils import check_project_owner
from utils.decorators import transaction_handler
from ScrumProjects.serializers import ScrumProjectSerializer
from Users.serializers import UserSerializer
from Users.utils import get_user_by_username_or_email

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
		username = serializers.CharField(required=False, write_only=True)
		email = serializers.CharField(required=False, write_only=True)
		user = UserSerializer(read_only=True)

		def validate(self, attrs):
			if 'scrum_project' in attrs:
				project = attrs.get('scrum_project')
			elif 'kanban' in attrs:
				pass
			else: raise ValidationError
			attrs['user'] = transaction_handler(get_user_by_username_or_email,
				{
					'username': attrs.get('username'),
					'email': attrs.get('email')
				})
			del attrs['username']
			del attrs['email']

			transaction_handler(check_project_owner,
				{'instance': project,
				'scrum': True,
				'user': self.context['request'].user}
			)
			transaction_handler(check_user_in_project,
				{'project':project,
				'user':attrs['user']
				}
			)
			transaction_handler(check_received_proposal,
				{'project':project,
				'user': attrs['user'],
				'scrum': True})
			return super().validate(attrs)


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