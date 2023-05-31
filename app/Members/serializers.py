from rest_framework import serializers

from Users.serializers import UserSerializer
from utils.decorators import transaction_handler

from .models import Member
from .utils import get_user_project, check_user_in_project, \
add_member, check_member_change_rool



class MemberSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Member
		fields = '__all__'


	class CreateSerializer(serializers.ModelSerializer):
		project = serializers.IntegerField(write_only=True)
		scrum = serializers.BooleanField(default=True) 

		def validate(self, attrs):
			attrs['project'] = transaction_handler(get_user_project,
				{'project': attrs['project'],
				'scrum': attrs['scrum'],
				'user': self.context['request'].user.id}
			)
			transaction_handler(check_user_in_project, 
				{'project':attrs['project'],
				'user': attrs['user'].id}
			)
			return super().validate(attrs)

		def create(self, validated_data):
			return transaction_handler(add_member, validated_data)


		class Meta:
			model = Member 
			fields = '__all__'

	class ChangeSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			transaction_handler(check_member_change_rool,
				{'instance':instance, 'user':self.context['request'].user.id})
			return super().update(instance, validated_data)

		class Meta:
			model = Member 
			fields = ['role']