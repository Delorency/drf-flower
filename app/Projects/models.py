from django.db import models
from django.contrib.auth import get_user_model

from utils.mixins import ObjMixin

from Workspaces.models import Workspace



class ProjectColumn(ObjMixin):
	number = models.PositiveIntegerField(verbose_name='Serial number')

	project = models.OneToOneField('Project', on_delete=models.CASCADE,
		related_name='project_projectcolumns', verbose_name='Column')

	class Meta:
		verbose_name_plural = 'Project columns'
		verbose_name = 'Project column'
		ordering = ('created_at',)



class Project(ObjMixin):

	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_projects', verbose_name='Creator')
	workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE,
		related_name="workspace_projects", verbose_name="Workspace")

	is_private = models.BooleanField(default=False, verbose_name="Is private")

	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		verbose_name_plural = 'Projects'
		verbose_name = 'Project'
		ordering = ('created_at',)