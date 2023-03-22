from rest_framework import serializers
from Users.serializers import UserSerializer



class CreatorSerializerHelper(serializers.ModelSerializer):

	creator = UserSerializer(read_only=True)

	def create(self, validated_data):
		validated_data['creator'] = self.context['request'].user
		return super().create(validated_data)