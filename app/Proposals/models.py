from django.db import models
from django.contrib.auth import get_user_model

from ScrumProjects.models import ScrumProject


class Proposal(models.Model):
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
		verbose_name='Role'
	)

	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_proposals', verbose_name='User')

	scrum_project = models.ForeignKey(ScrumProject, on_delete=models.CASCADE,
		null=True, blank=True, related_name='scrumproject_proposals',
		verbose_name='Scrum project')

	created_at = models.DateTimeField(auto_now_add=True,
		verbose_name='Created at')


	def __str__(self):
		return f'id: {self.id} | user: {self.user} | scrum: {self.scrum_project}'


	class Meta:
		verbose_name_plural = 'Proposals'
		verbose_name = 'Proposal'
		ordering = ('-created_at',)