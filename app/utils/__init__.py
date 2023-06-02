def check_project_owner(data):
	if data.get('scrum'):
		data.get('instance').team.filter(
			user=data.get('user')).get(role='Project owner')