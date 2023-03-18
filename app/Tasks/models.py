from django.db import models
from django.contrib.auth import get_user_model

from utils.mixins import ObjMixin



class CheckList_item(ObjMixin):
	executor = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
		related_name='user_checklistitem', null=True, blank=True, 
		verbose_name='Executor')

	date = models.DateTimeField(null=True, blank=True, verbose_name='Date')

	done = models.BooleanField(default=False, verbose_name='Done')

	taskcard = models.OneToOneField('TaskCard', on_delete=models.CASCADE,
		related_name='taskcard_checklistitem', verbose_name='TaskCard')


	class Meta:
		verbose_name_plural = 'CheckList_items'
		verbose_name = 'CheckList_item'
		ordering = ('updated_at',)


class TaskCard(ObjMixin):

	description = models.CharField(max_length=1000,
		verbose_name='Description')

	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_taskcard', verbose_name='Creator')

	date = models.DateTimeField(null=True, blank=True, verbose_name='Date')

	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		verbose_name_plural = 'TaskCards'
		verbose_name = 'TaskCard'
		ordering = ('created_at',)