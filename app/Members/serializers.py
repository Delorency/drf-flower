from rest_framework import serializers

from Users.serializers import UserSerializer

from .models import Member



class MemberSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Member
		fields = '__all__'


	class CreateSerializer(serializers.ModelSerializer):
		project = serializers.IntegerField(write_only=True)
		scrum = serializers.BooleanField(default=True) 

		def validate(self, attrs):
			try:
				attrs['project'] = \
				self.context['request'].user.get_user_project(attrs['project'],
					scrum)
				return super().validate(attrs) 
			except:
				raise PermissionDenied()

		def create(self, validated_data):
			try:
				with transaction.atomic():
					return add_member(validated_data)
			except:
				raise NotFound()


		class Meta:
			model = Member 
			fields = '__all__'