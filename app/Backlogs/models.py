from django.db import models

from utils.mixins import ObjMixin
from ScrumProjects.models import ScrumProject
from Tasks.models import Task



class Backlog(ObjMixin):
	DIFFICULT = [
		("Easy", "Easy"),
		("Medium", "Medium"),
		("Hard", "Hard")
	]
	difficult = models.CharField(max_length=20, choices=DIFFICULT)

	scrum_project = models.ForeignKey(ScrumProject, on_delete=models.CASCADE,
		related_name='scrumproject_backlogs', verbose_name='Scrum project')

	tasks = models.ManyToManyField(Task, blank=True,
		related_name='task_backlogs', verbose_name='Tasks')

	in_sprint = models.BooleanField(default=False, verbose_name='In sprint')


	def __str__(self):
		return f'id: {self.id} | difficult: {self.difficult}'

	class Meta:
		verbose_name_plural = 'Backlogs'
		verbose_name = 'Backlog'
		ordering = ('-created_at',)
