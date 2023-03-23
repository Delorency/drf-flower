from .models import *



def create_new_column(data):
	project = data.pop('project')
	column = ProjectColumn.objects.create(**data)
	project.columns.add(column)
	project.save()

	return column