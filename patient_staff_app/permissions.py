from rest_framework import permissions

class IsHealthWorker(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        
        if user.is_superuser:
            return True
        
        return user.is_authenticated and user.groups.filter(name='HealthWorkers').exists()
    
    
class CanViewPatients(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        
        if user.is_superuser:
            return True
        
        return user.is_authenticated and user.groups.filter(name='HealthWorkers').exists()
    

        