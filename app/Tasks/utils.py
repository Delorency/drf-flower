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