from rest_framework import serializers

from utils.decorators import transaction_handler
from utils.exceptions import MyError
from Members.serializers import MemberSerializer

from .models import *
from .utils import *



class TaskItemSerializer(serializers.ModelSerializer):
	worker = MemberSerializer()

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
			if 'worker' in attrs:
				transaction_handler(check_member_in_workers,
					{
					'task' : attrs['task'],
					'member': attrs['worker']
					},
					MyError('worker', 'Worker must be in task team', 400))
			return super().validate(attrs)

		def create(self, validated_data):
			return transaction_handler(add_task_item,
				{'task':validated_data['task'],
				 **validated_data
				})

		class Meta:
			model = TaskItem
			fields = ['id', 'name', 'task', 'worker']


	class UpdateSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if 'worker' in validated_data:

				transaction_handler(check_member_in_workers,
					{
					'task' :instance.taskitem_tasks.first(),
					'member': validated_data['worker']
					},
					MyError('worker', 'Worker must be in task team', 400))

			if 'end_at' in validated_data:

				transaction_handler(check_taskitems_date,
					{
					'task' :instance.taskitem_tasks.first(),
					'end_at': validated_data['end_at']
					},
					MyError('end_at', 'Task item end date must be lower then task end date', 400))

			return super().update(instance, validated_data)

		class Meta:
			model = TaskItem
			fields = '__all__'

	class RemoveWorkerSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			instance.worker = None
			instance.save()
			return instance

		class Meta:
			model = TaskItem
			fields = ['worker']


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

			if 'end_at' in attrs:

				transaction_handler(valid_end_at_date, {
					'instance':attrs['backlog'],
					'end_at':attrs['end_at']
					},
					MyError('end_at', 'Task end date must be in sprint time interval', 400))

			return super().validate(attrs)

		def create(self, validated_data):
			return transaction_handler(add_task, validated_data)

		class Meta:
			model = Task 
			fields = ['id', 'name', 'description', 'color', 'column', 'end_at', 'backlog']


	class UpdateSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if 'column' in validated_data:
				if validated_data['column'] == Task.COLUMN[0][0] \
				or validated_data['column'] == Task.COLUMN[1][0]:
					instance.close = False
			if 'end_at' in validated_data:
				transaction_handler(valid_end_at_date, {
					'instance':instance.task_backlogs.first(),
					'end_at':validated_data['end_at']
					},
					MyError('end_at', 'Task end date must be in sprint time interval', 400))
				instance.end_at = validated_data['end_at']
				instance.save()
				validated_data.pop('end_at')
				transaction_handler(convert_to_right_data, {'instance':instance})

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