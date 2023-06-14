from rest_framework.permissions import BasePermission



class CreatorFieldHelperPermission(BasePermission):
    def has_permission(self, request, view):
        request.POST._mutable = True
        request.data['creator'] = request.user.id
        return True


        
class ProjectChangePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return obj.team.filter(user=request.user).exists()
        return obj.team.filter(user=request.user, role='Project owner').exists()