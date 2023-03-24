from .models import TaskCard


def create_new_taskcard(data):
	project = data.pop('project')
	taskcard = TaskCard.objects.create(**data)
	project.tasks.add(taskcard)
	project.save()

	return taskcard