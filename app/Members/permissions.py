from rest_framework.permissions import BasePermission



class MemberChangePermission(BasePermission):

	def has_object_permission(self, request, view, obj):
		return obj.member_scrumprojects.first().team.filter(
		user=request.user, role='Project owner').exists()