from ScrumProjects.models import ScrumProject

from .models import Member



def check_user_rool(data):
	data.get('user').user_members.filter(
		role='Project owner').get(scrum_project=data.get('project'))


def add_member(data):
	project = data.pop('project')
	instance = data.pop('instance')

	member = Member.objects.create(
		**data
	)
	project.team.add(member)
	project.save()
	instance.delete()
	return member