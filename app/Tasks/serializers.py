from rest_framework import serializers

from utils.decorators import transaction_handler
from Members.serializers import MemberSerializer

from .models import *
from .utils import check_project_owner_backlog, check_user_in_project,\
add_task, check_member_in_project



class TaskSerializer(serializers.ModelSerializer):
	worker = MemberSerializer()

	class Meta:
		model = Task 
		fields = '__all__'


	class CreateSerializer(serializers.ModelSerializer):
		backlog = serializers.IntegerField(write_only=True)

		def validate(self, attrs):
			attrs['backlog'] = transaction_handler(check_project_owner_backlog, 
				{
				'backlog': attrs['backlog'],
				'user': self.context['request'].user
				})
			if 'worker' in attrs:
				transaction_handler(check_member_in_project,
					{
					'project' :attrs['backlog'].scrum_project,
					'member': attrs['worker']
					})
			return super().validate(attrs)

		def create(self, validated_data):
			return transaction_handler(add_task, validated_data)

		class Meta:
			model = Task 
			fields = '__all__'


	class UpdateSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if 'worker' in validated_data:
				transaction_handler(check_member_in_project,
					{
					'project' :\
					instance.task_backlogs.first().scrum_project,
					'member': validated_data['worker']
					})
			return super().update(instance, validated_data)

		class Meta:
			model = Task 
			fields = ['id', 'description', 'color', 'column', 'end_at',
			'worker']


	class TaskChangeColumnSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if 'column' in validated_data:

				if (instance.column == Task.COLUMN[0][0] \
				and validated_data['column'] == Task.COLUMN[1][0]) \
				or \
				(instance.column == Task.COLUMN[1][0] \
				and validated_data['column'] == Task.COLUMN[2][0]):
					pass
				else:
					validated_data.pop('column')


			return super().update(instance, validated_data)


		class Meta:
			model = Task 
			fields = ['column']