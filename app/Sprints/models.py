from django.db import models

from ScrumProjects.models import ScrumProject
from Backlogs.models import Backlog



class Sprint(models.Model):
	start_at = models.DateField(verbose_name='Start at')
	end_at = models.DateField(verbose_name='End at')

	scrum_project = models.ForeignKey(ScrumProject, on_delete=models.CASCADE,
		related_name='scrumproject_sprints', verbose_name='Scrum project')

	backlogs = models.ManyToManyField(Backlog, blank=True, 
		related_name='backlog_sprints', verbose_name='Backlog')


	def __str__(self):
		return f'id: {self.id} | start_at: {self.start_at} | end_at: {self.end_at}'

	class Meta:
		verbose_name_plural = 'Sprints'
		verbose_name = 'Sprint'
		ordering = ('-end_at',)