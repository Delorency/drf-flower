from rest_framework.permissions import BasePermission



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