from django.db import models
from django.contrib.auth import get_user_model

from utils.mixins import ObjMixin



# class CheckList_item(ObjMixin):
# 	date = models.DateTimeField(null=True, blank=True, verbose_name='Date')

# 	done = models.BooleanField(default=False, verbose_name='Done')

# 	taskcard = models.OneToOneField('TaskCard', on_delete=models.CASCADE,
# 		related_name='taskcard_checklistitems', verbose_name='TaskCard')

# 	def __str__(self):
# 		return f'id: {self.id}'


# 	class Meta:
# 		verbose_name_plural = 'CheckList_items'
# 		verbose_name = 'CheckList_item'
# 		ordering = ('updated_at',)
class ProjectColumn(ObjMixin):
	number = models.PositiveIntegerField(verbose_name='Serial number')

	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_projectcolumn_creators', verbose_name='Creator')	

	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		verbose_name_plural = 'Project columns'
		verbose_name = 'Project column'
		ordering = ('created_at',)

		

class TaskCard(ObjMixin):

	description = models.CharField(max_length=1000, null=True, blank=True,
		verbose_name='Description')
	column = models.ForeignKey(ProjectColumn, on_delete=models.CASCADE,
		related_name='projectcolumn_taskcards', verbose_name='Column')
	worker = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
		related_name='user_taskcard_workers', null=True, blank=True,
		verbose_name='Worker')
	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_taskcard_creators', verbose_name='Creator')

	date = models.DateTimeField(null=True, blank=True, verbose_name='Date')


	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		verbose_name_plural = 'TaskCards'
		verbose_name = 'TaskCard'
		ordering = ('created_at',)