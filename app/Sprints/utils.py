def get_valid_backlogs(data):
	instance = data.get('instance')
	return [ item for item in data.get('backlogs')
	if item.scrum_project == instance.scrum_project]
