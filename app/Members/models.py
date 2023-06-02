from django.db import models
from django.contrib.auth import get_user_model

from ScrumProjects.models import ScrumProject



class Member(models.Model):
	ROLES = [
		("Backend", "Backend"),
		("Frontend", "Frontend"),
		("Design", "Design"),
		("Stakeholder", "Stakeholder"),
		("UX", "UX"),
		("Project owner", "Project owner")
	]
	role = models.CharField(
		max_length=20,
		choices=ROLES,
	)

	scrum_project = models.ForeignKey(ScrumProject, on_delete=models.CASCADE,
		null=True, blank=True, related_name='scrumproject_members',
		verbose_name='Scrum project')

	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, 
		related_name='user_members', verbose_name='User')

	created_at = models.DateTimeField(auto_now_add=True,
		verbose_name='Created at')


	def __str__(self):
		return f'id: {self.id} | name: {self.user.username} | role: {self.role}'

	class Meta:
		verbose_name_plural = 'Members'
		verbose_name = 'Member'
		ordering = ('-created_at',)