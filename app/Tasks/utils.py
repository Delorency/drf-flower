from utils import check_user_in_project as u_check_user_in_project

from Backlogs.models import Backlog

from .models import *



def check_project_owner_backlog(data):
	backlog = Backlog.objects.get(id=data.get('backlog'))

	backlog.scrum_project.team.get(user=data.get('user'))

	return backlog


def check_user_in_project(data):
	if not u_check_user_in_project(data):
		raise ValueError
	return None


def check_member_in_project(data):
	data.get('project').team.get(id=data.get('member').id)


def add_task(data):
	backlog = data.pop('backlog')
	task = Task.objects.create(**data)
	backlog.tasks.add(task)
	backlog.save()

	return task


def checkGet_task(data):
	task = Task.objects.get(id=data.get('task'))
	project = task.task_backlogs.first().scrum_project
	if project.team.filter(user=data.get('user'),
		role='Project owner'):
		return task


def add_task_item(data):
	task = data.pop('task')

	task_item = TaskItem.objects.create(**data)
	task.task_items.add(task_item)
	task.save()

	return task_item


def check_taskitems_date(data):
	task = data.get('instance').taskitem_tasks.first()

	if task.end_at:
		if data.get('end_at') > task.end_at: 
			raise ValueError


def check_member_in_workers(data):
	data.get('task').workers.get(id=data.get('member').id)


def add_worker(data):
	instance = data.get('instance')
	instance.workers.add(data.get('member'))
	instance.save()
	return instance


def remove_worker(data):
	instance = data.get('instance')
	instance.workers.remove(data.get('member'))
	for item in instance.task_items.all():
		item.worker = None
		item.save()
	instance.save()
	return instance


def valid_end_at_date(data):
	backlog = data.get('instance')
	sprint = backlog.backlog_sprints.first()
	sprint_end_at = sprint.end_at
	sprint_start_at = sprint.start_at

	if not (sprint_start_at <= data.get('end_at') <= sprint_end_at):
		raise ValueError


def convert_to_right_data(data):
	task = data.get('instance')

	for item in task.task_items.all():
		if item.end_at > task.end_at:
			item.end_at = task.end_at
			item.save() 