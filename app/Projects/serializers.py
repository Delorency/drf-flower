from django.db import transaction
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.serializers import IntegerField

from djoser.serializers import UserSerializer as dj_UserSerializer

from Users.serializers import UserSerializer

from .models import *



class MemberSerializer(serializers.ModelSerializer):
	creator = UserSerializer()

	class Meta:
		model = Member
		fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):
	creator = UserSerializer()
	team = MemberSerializer(many=True)

	class Meta:
		model = Project
		fields = '__all__'


	class CreateSerializer(serializers.ModelSerializer):
		creator = dj_UserSerializer(read_only=True)

		def validate(self, attrs):
			attrs['creator'] = self.context['request'].user
			return super().validate(attrs) 

		def create(self, validated_data):
			try:
				with transaction.atomic():
					return create_new_project(validated_data)
			except:
				raise NotFound()

		class Meta:
			model = Project
			fields = ('id', 'name', 'creator', 'workspace', 
			'is_private', 'created_at', 'updated_at')

class ProjectSerializer(serializers.ModelSerializer):
	tasks = TaskCardSerializer(many=True)
	workspace = WorkspaceSerializer()

	class Meta:
		model = Project
		fields = ('id', 'name', 'creator', 'tasks', 'workspace', 
			'is_private', 'created_at', 'updated_at')

	class CreateSerializer(CreatorForCreateSerializerHelper):

		def validate(self, attrs):
			attrs['creator'] = self.context['request'].user
			if not attrs['workspace'].check_creator(attrs['creator']):  
				raise PermissionDenied()
			return super().validate(attrs) 

		class Meta:
			model = Project
			fields = ('id', 'name', 'creator', 'workspace', 
			'is_private', 'created_at', 'updated_at')

	class RetrieveUpdateDestroySerializer(CreatorForChangeSerializerHelper):

		class Meta:
			model = Project
			fields = ('id', 'name', 'creator', 'is_private', 'created_at',
				'updated_at')

	class MyListSerializer(CreatorForChangeSerializerHelper):
		tasks = TaskCardSerializer(many=True)
		workers = MyUserSerializer(many=True)
		workspace = WorkspaceSerializer()
		
		class Meta:
			model = Project
			fields = '__all__'