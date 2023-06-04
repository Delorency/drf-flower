from ScrumProjects.models import ScrumProject

from .models import Backlog



def check_project_owner(data):
	data.get('scrum_project').team.filter(user=data.get('user')).get(
		role='Project owner')


def check_user_in_team(data):
	ScrumProject.objects.get(
		id=data.get('scrum_project')).team.get(user=data.get('user'))