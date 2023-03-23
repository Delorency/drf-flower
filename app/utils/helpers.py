from rest_framework import serializers
from djoser.serializers import UserSerializer as djoser_UserSerializer

from Users.serializers import UserSerializer



class CreatorForListSerializerHelper(serializers.ModelSerializer):
	creator = UserSerializer()


class CreatorForCreateSerializerHelper(serializers.ModelSerializer):
	creator = djoser_UserSerializer(read_only=True)


class CreatorForChangeSerializerHelper(serializers.ModelSerializer):
	creator = djoser_UserSerializer(read_only=True)