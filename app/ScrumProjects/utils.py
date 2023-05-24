from Members.models import Member

from .models import Project


def create_new_project(validated_data):
	member = Member.objects.create(
		role=Member.COLUMNS[-1],
		user=validated_data.get('creator')
	)
	validated_data['team'] = [member]
	project = Project.objects.create(**validated_data)

	return project