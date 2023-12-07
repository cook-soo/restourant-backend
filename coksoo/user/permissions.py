from rest_framework import permissions
from user.models import Manager

class IsManager(permissions.BasePermission):
    message = "Idi nahui"
    
    def has_permission(self, request, view):
        return Manager.objects.filter(user=request.user).exists()

