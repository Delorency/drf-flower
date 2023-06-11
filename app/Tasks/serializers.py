from rest_framework import serializers

from utils.decorators import transaction_handler
from Members.serializers import MemberSerializer

from .models import *
from .utils import *



class TaskItemSerializer(serializers.ModelSerializer):

	class Meta:
		model = TaskItem
		fields = '__all__'

	class CreateSerializer(serializers.ModelSerializer):
		task = serializers.IntegerField(write_only=True)

		def validate(self, attrs):
			attrs['task'] = transaction_handler(checkGet_task,
				{'task':attrs['task'],
				 'user':self.context['request'].user
				})
			return super().validate(attrs)

		def create(self, validated_data):
			return transaction_handler(add_task_item,
				{'task':validated_data['task'],
				 **validated_data
				})

		class Meta:
			model = TaskItem
			fields = ['id', 'name', 'task']


	class UpdateSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if 'worker' in validated_data:
				transaction_handler(check_member_in_workers,
					{
					'task' :instance.taskitem_tasks.first(),
					'member': validated_data['worker']
					})
			if 'end_at' in validated_data:
				transaction_handler(check_taskitems_date,
					{
					'instance' :instance,
					'end_at': validated_data['end_at']
					})
			return super().update(instance, validated_data)

		class Meta:
			model = TaskItem
			fields = '__all__'


	class CloseSerializer(serializers.ModelSerializer):

		class Meta:
			model = TaskItem
			fields = ['close']



class TaskSerializer(serializers.ModelSerializer):
	workers = MemberSerializer(many=True)
	task_items = TaskItemSerializer(many=True)

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
			if 'workers' in attrs:
				transaction_handler(check_members_in_project,
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
			if 'column' in validated_data:
				if validated_data['column'] == Task.COLUMN[0][0] \
				or validated_data['column'] == Task.COLUMN[1][0]:
					instance.close = False
			if 'workers' in validated_data:
				transaction_handler(check_member_in_project,
					{
					'project' :\
					instance.task_backlogs.first().scrum_project,
					'member': validated_data['worker']
					})
			return super().update(instance, validated_data)

		class Meta:
			model = Task 
			fields = ['id', 'description', 'color', 'column', 'end_at']


	class AddWorkerSerializer(serializers.ModelSerializer):
		add = serializers.BooleanField(write_only=True)

		def update(self, instance, validated_data):
			transaction_handler(check_member_in_project,
				{
				'project' :\
				instance.task_backlogs.first().scrum_project,
				'member': validated_data['workers'][0]
				})
			if validated_data['add']:
				return transaction_handler(add_worker,
					{'instance':instance,
					 'member':validated_data['workers'][0]
					})
			else:
				return transaction_handler(remove_worker,
					{'instance':instance,
					 'member':validated_data['workers'][0]
					})
		class Meta:
			model = Task 
			fields = ['workers', 'add']


	class TaskChangeColumnSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if 'column' in validated_data:

				if (instance.column == Task.COLUMN[0][0] \
				and validated_data['column'] == Task.COLUMN[1][0]):
					pass

				elif (instance.column == Task.COLUMN[1][0] \
				and validated_data['column'] == Task.COLUMN[2][0]):
					instance.close = True
				else:
					validated_data.pop('column')


			return super().update(instance, validated_data)


		class Meta:
			model = Task 
			fields = ['column']