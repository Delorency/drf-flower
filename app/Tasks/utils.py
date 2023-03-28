from .models import *


def create_new_taskcard(data):
	project = data.pop('project')
	taskcard = TaskCard.objects.create(**data)
	project.tasks.add(taskcard)
	project.save()

	return taskcard


def create_new_column(data):
	project = data.pop('project')
	column = ProjectColumn.objects.create(**data)
	project.columns.add(column)
	project.save()

	return column