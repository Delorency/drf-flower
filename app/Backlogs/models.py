from django.db import models

from utils.mixins import ObjMixin



class Backlog(ObjMixin):
	DIFFICULT = [
		("Easy", "Easy"),
		("Medium", "Medium"),
		("Hard", "Hard")
	]
	difficult = models.CharField(max_length=20, choices=DIFFICULT)

	start_at = models.DateField(verbose_name='Start at')
	end_at = models.DateField(verbose_name='End at')


	def __str__(self):
		return f'id: {self.id} | difficult: {self.difficult} | \
		start_at: {self.start_at}| end_at: {self.end_at}'

	class Meta:
		verbose_name_plural = 'Backlogs'
		verbose_name = 'Backlog'
		ordering = ('-created_at',)
