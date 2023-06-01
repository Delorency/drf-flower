from .models import Backlog



def add_backlog(data):
	project = data.pop('project')
	backlog = Backlog.objects.create(
		**data	
	)
	project.backlogs.add(backlog)
	project.save()
	return backlog