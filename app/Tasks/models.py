from django.db import models

from utils.mixins import ObjMixin
from Members.models import Member



class TaskItem(ObjMixin):
	end_at = models.DateField(null=True, blank=True, verbose_name='End at')
	worker = models.ForeignKey(Member, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='member_taskitems', verbose_name='Worker')
	close = models.BooleanField(default=False)


	def __str__(self):
		return f'id: {self.id} | end_at: {self.end_at}'

	class Meta:
		verbose_name_plural = 'TaskItems'
		verbose_name = 'TaskItem'
		ordering = ('-created_at',)


		
class Task(ObjMixin):
	COLUMN = (
		('To Do', 'To Do'),
		('In Progress', 'In Progress'),
		('In Review', 'In Review'),
		('Done', 'Done'),
		('Archive', 'Archive')
	)

	description = models.CharField(max_length=1000, verbose_name='Description')
	color = models.CharField(max_length=7, null=True, blank=True, verbose_name='Color')

	column = models.CharField(max_length=30, choices=COLUMN, default='To Do',
		verbose_name='Column')
	
	end_at = models.DateField(null=True, blank=True, verbose_name='End at')

	workers = models.ManyToManyField(Member,related_name='member_tasks',
		blank=True, verbose_name='Workers')

	task_items = models.ManyToManyField(TaskItem, blank=True,
		related_name='taskitem_tasks', verbose_name='Task items')

	close = models.BooleanField(default=False, verbose_name='Close')


	def __str__(self):
		return f'id: {self.id} | end_at: {self.end_at}'

	class Meta:
		verbose_name_plural = 'Tasks'
		verbose_name = 'Task'
		ordering = ('-created_at',)