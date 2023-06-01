from rest_framework.permissions import BasePermission


class CreatorFieldHelperPermission(BasePermission):
    def has_permission(self, request, view):
        request.POST._mutable = True
        request.POST['creator'] = request.user.id
        return True



class ProjectUpdatePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.team.filter(user=request.user, role='Project owner').exists()








class ChangeObjectPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class GetProjectPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.workers.all() or obj.creator == request.user


class ChangeObjectForProposalPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user



class ChangeObjectForTaskCardPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or obj.worker == request.user