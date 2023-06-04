def check_project_owner(data):
	if data.get('scrum'):
		data.get('instance').team.filter(
			user=data.get('user')).get(role='Project owner')


def check_user_in_project(data):
	return data.get('project').team.filter(user=data.get('user')).exists()