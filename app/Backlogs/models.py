from django.db import models

from utils.mixins import ObjMixin
from ScrumProjects.models import ScrumProject



class Backlog(ObjMixin):
	DIFFICULT = [
		("Easy", "Easy"),
		("Medium", "Medium"),
		("Hard", "Hard")
	]
	difficult = models.CharField(max_length=20, choices=DIFFICULT)

	scrum_project = models.ForeignKey(ScrumProject, on_delete=models.CASCADE,
		related_name='scrumproject_backlogs', verbose_name='Scrum project')

	def __str__(self):
		return f'id: {self.id} | difficult: {self.difficult}'

	class Meta:
		verbose_name_plural = 'Backlogs'
		verbose_name = 'Backlog'
		ordering = ('-created_at',)
