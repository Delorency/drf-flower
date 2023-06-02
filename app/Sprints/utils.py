def get_valid_backlogs(data):
	instance = data.get('instance')
	p_backlogs = instance.scrum_project.backlogs.all()
	return [ item for item in data.get('backlogs') if item in p_backlogs]
