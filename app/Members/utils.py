from ScrumProjects.models import ScrumProject

from .models import Member



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