from django.db import models
from django.contrib.auth import get_user_model

from utils.mixins import ObjMixin

from Members.models import Member



class ScrumProject(ObjMixin):
	description = models.CharField(max_length=1000, verbose_name='Description')
	
	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_scrumproject', verbose_name='Creator')

	team = models.ManyToManyField(Member, related_name='member_scrumprojects',
		blank=True, verbose_name='Team')

	is_private = models.BooleanField(default=False, verbose_name='Is private')
	is_scrum = models.BooleanField(default=True, verbose_name='Is scrum')


	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'

	class Meta:
		verbose_name_plural = 'ScrumProjects'
		verbose_name = 'ScrumProject'
		ordering = ('-created_at',)  