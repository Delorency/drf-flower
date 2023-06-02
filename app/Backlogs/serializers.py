from rest_framework import serializers

from utils.decorators import transaction_handler
from ScrumProjects.utils import get_project_owner

from .models import Backlog
from .utils import add_backlog



class BacklogSerializer(serializers.ModelSerializer):

	class Meta:
		model = Backlog 
		fields = '__all__'

	class CreateSerializer(serializers.ModelSerializer):
		project = serializers.IntegerField(write_only=True)

		def validate(self, attrs):
			attrs['project'] = transaction_handler(get_project_owner,
				{'project': attrs['project'],
				 'user': self.context['request'].user
				}
			)
			return super().validate(attrs)

		def create(self, validated_data):
			return transaction_handler(add_backlog, validated_data)

		class Meta:
			model = Backlog
			fields = '__all__'

	class ChangeSerializer(serializers.ModelSerializer):

		class Meta:
			model = Backlog 
			fields = '__all__'