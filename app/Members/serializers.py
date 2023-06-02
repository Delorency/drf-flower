from rest_framework import serializers

from Users.serializers import UserSerializer
from ScrumProjects.serializers import ScrumProjectSerializer
from utils import user_in_project
from utils.decorators import transaction_handler

from .models import Member
from .utils import check_user_rool



class MemberSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	scrum_project = ScrumProjectSerializer()

	class Meta:
		model = Member
		fields = '__all__'

	class CreateSerializer(serializers.ModelSerializer):

		def validate(self, attrs):
			transaction_handler(check_user_rool,
				{'project': attrs['scrum_project'],
				 'user': self.context['user']})
			transaction_handler(user_in_project,
				{'project': attrs['scrum_project'],
				 'user': self.context['user']})
			return super().validate(attrs)


	class ChangeSerializer(serializers.ModelSerializer):

		class Meta:
			model = Member 
			fields = ['role']