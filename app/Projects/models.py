from django.db import models
from django.contrib.auth import get_user_model

from utils.mixins import ObjMixin

from Workspaces.models import Workspace
from Tasks.models import TaskCard



class Project(ObjMixin):
	date = models.DateField(null=True, blank=True, verbose_name='Date')

	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_project_creators', verbose_name='Creator')
	workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE,
		related_name='workspace_projects', verbose_name="Workspace")

	workers = models.ManyToManyField(get_user_model(),
		related_name='user_project_workers', blank=True, 
		verbose_name='Workers')
	tasks = models.ManyToManyField(TaskCard, related_name="taskcard_projects",
		blank=True, verbose_name='Tasks')

	is_private = models.BooleanField(default=False, verbose_name='Is private')

	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'

	def check_creator(self, user):
		return self.creator == user

	def has_worker(self, user):
		return user in self.project.workers


	class Meta:
		verbose_name_plural = 'Projects'
		verbose_name = 'Project'
		ordering = ('-created_at',)



class Proposal(models.Model):
	message = models.CharField(max_length=500, null=True, blank=True,
		verbose_name='Message')
	
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_proposal_users', verbose_name='User')
	project = models.ForeignKey(Project, on_delete=models.CASCADE,
		related_name='project_proposal', verbose_name='Project')
	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_proposal_creators', verbose_name='Creator')

	created_at = models.DateTimeField(auto_now_add=True,
		verbose_name='Created at')
	updated_at = models.DateTimeField(auto_now=True,
		verbose_name='Updated at')

	def __str__(self):
		return f'id: {self.id} | project: {self.project}'


	class Meta:
		verbose_name_plural = 'Proposals'
		verbose_name = 'Proposal'
		ordering = ('-created_at',)