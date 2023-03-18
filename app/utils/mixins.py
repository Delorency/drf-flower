from django.db import models



class ObjMixin(models.Model):
	name = models.CharField(max_length=100, verbose_name='Name')
	created_at = models.DateTimeField(auto_now_add=True,
		verbose_name='Created at')
	updated_at = models.DateTimeField(auto_now=True,
		verbose_name='Updated at')


	class Meta:
		abstract = True