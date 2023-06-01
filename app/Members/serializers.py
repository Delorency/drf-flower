from rest_framework import serializers

from Users.serializers import UserSerializer

from .models import Member



class MemberSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Member
		fields = '__all__'

	class ChangeSerializer(serializers.ModelSerializer):

		class Meta:
			model = Member 
			fields = ['role']