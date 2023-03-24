from django.db import models
from django.contrib.auth import get_user_model

from utils.mixins import ObjMixin

from Workspaces.models import Workspace
from Tasks.models import TaskCard



class ProjectColumn(ObjMixin):
	number = models.PositiveIntegerField(verbose_name='Serial number')

	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_projectcolumns', verbose_name='Creator')	

	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		verbose_name_plural = 'Project columns'
		verbose_name = 'Project column'
		ordering = ('created_at',)



class Project(ObjMixin):
	date = models.DateTimeField(null=True, blank=True, verbose_name='Date')

	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_projects', verbose_name='Creator')
	workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE,
		related_name='workspace_projects', verbose_name="Workspace")

	columns = models.ManyToManyField(ProjectColumn,
		related_name='projectcolumn_projects', blank=True, 
		verbose_name='Columns')

	tasks = models.ManyToManyField(TaskCard, related_name="taskcard_projects",
		blank=True, verbose_name='Tasks')

	is_private = models.BooleanField(default=False, verbose_name='Is private')

	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		verbose_name_plural = 'Projects'
		verbose_name = 'Project'
		ordering = ('created_at',)