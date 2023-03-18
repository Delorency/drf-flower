from django.db import models
from django.contrib.auth import get_user_model

from utils.mixins import ObjMixin



class Workspace(ObjMixin):

	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_workspaces', verbose_name='Creator')

	marked = models.BooleanField(default=False, verbose_name='Marked')
	is_private = models.BooleanField(default=False, verbose_name="Is private")

	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		verbose_name_plural = 'Workspaces'
		verbose_name = 'Workspace'
		ordering = ('created_at',)
	