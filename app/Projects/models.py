from django.db import models
from django.contrib.auth import get_user_model

from utils.mixins import ObjMixin



class Member(models.Model):
	COLUMNS = [
		("Backend", "Backend"),
		("Frontend", "Frontend"),
		("Design", "Design"),
		("Stakeholder", "Stakeholder"),
		("UX", "UX"),
		("Product owner", "Product owner")
	]
	role = models.CharField(
		max_length=10,
		choices=COLUMNS,
	)

	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, 
		related_name='user_member', verbose_name='User')

	created_at = models.DateTimeField(auto_now_add=True,
		verbose_name='Created at')


	def __str__(self):
		return f'id: {self.id} | name: {self.user.username} | role: {self.role}'

	class Meta:
		verbose_name_plural = 'Members'
		verbose_name = 'Member'
		ordering = ('-created_at',)



class Project(ObjMixin):
	description = models.CharField(max_length=1000, verbose_name='Description')
	
	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_project_creators', verbose_name='Creator')

	team = models.ManyToManyField(Member
		related_name='member_projects', verbose_name='Team')

	is_private = models.BooleanField(default=False, verbose_name='Is private')
	is_scrum = models.BooleanField(default=True, verbose_name='Is scrum')


	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'

	class Meta:
		verbose_name_plural = 'ScrumProjects'
		verbose_name = 'ScrumProject'
		ordering = ('-created_at',)