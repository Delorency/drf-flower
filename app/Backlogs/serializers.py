from rest_framework import serializers

from utils.decorators import transaction_handler
from ScrumProjects.serializers import ScrumProjectSerializer

from .models import Backlog
from .utils import check_project_owner



class BacklogSerializer(serializers.ModelSerializer):

	class Meta:
		model = Backlog 
		fields = '__all__'

	class CreateSerializer(serializers.ModelSerializer):

		def validate(self, attrs):
			transaction_handler(check_project_owner,
				{'scrum_project': attrs['scrum_project'],
				 'user': self.context['request'].user
				}
			)
			return super().validate(attrs)

		class Meta:
			model = Backlog
			fields = ['id', 'name', 'difficult', 'scrum_project']

	class ChangeSerializer(serializers.ModelSerializer):

		class Meta:
			model = Backlog 
			fields = ['id', 'difficult', 'name']