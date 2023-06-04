from rest_framework.permissions import BasePermission



class BacklogChangePermission(BasePermission):

	def has_object_permission(self, request, view, obj):
		return obj.scrum_project.team.filter(user=request.user,
			role='Project owner').exists()