from Members.models import Member

from .models import ScrumProject



def create_new_project(validated_data):
	member = Member.objects.create(
		role=Member.COLUMNS[-1][-1],
		user=validated_data.get('creator')
	)
	project = ScrumProject.objects.create(**validated_data)
	project.team.add(member)
	project.save()

	return project


def delete_project(instance):
	for i in instance.team.all():
		i.delete()
	instance.delete()