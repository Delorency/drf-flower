from ScrumProjects.models import ScrumProject

from .models import Member



def get_user_project(data):
	if data.get('scrum'):
		project = ScrumProject.objects.prefetch_related('team').get(id=data.get('project'))
	else:
		pass
	project.team.filter(user__id=data.get('user')).get(role='Project owner')
	return project


def check_user_in_project(data):
	if data.get('project').team.filter(user__id=data['user']).exists():
		raise ValueError
	return None


def add_member(validated_data):
	project, _ = validated_data.pop('project'), validated_data.pop('scrum')
	member = Member.objects.create(
		**validated_data
	)
	project.team.add(member)
	project.save()

	return member


def check_member_change_rool(data):
	data.get('instance').member_scrumprojects.first().team.filter(
		user__id=data.get('user')).get(role='Project owner')
