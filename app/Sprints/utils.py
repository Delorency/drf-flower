def save_valid_backlogs(data):
	instance = data.get('instance')
	for item in data.get('backlogs'):
		if item.scrum_project == instance.scrum_project:
			instance.backlogs.add(item)
			item.in_sprint = True
			item.save()

	instance.save()
	return instance



def remove_valid_backlogs(data):
	instance = data.get('instance')
	for item in data.get('backlogs'):
		if item in instance.backlogs.all():
			instance.backlogs.remove(item)
			item.in_sprint = False
			item.save()

	instance.save()
	return instance
