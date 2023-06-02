from Members.models import Member

from .models import ScrumProject



def create_new_project(validated_data):
	project = ScrumProject.objects.create(**validated_data)
	validated_data['scrum_project'] = project

	member = Member.objects.create(
		role=Member.COLUMNS[-1][-1],
		user=validated_data.get('creator')
	)

	return project


def delete_project(instance):
	for i in instance.scrumproject_members.all():
		i.delete()
	instance.delete()


def get_project_owner(data):
	project = ScrumProject.objects.prefetch_related('team').get(
		id=data.get('project'))
	project.team.filter(user=data.get('user')).get(role='Project owner')

	return project