def user_in_project(data):
	if data.get('user').user_members.filter(
		scrum_project=data.get('project')).exists():
		raise ValueError