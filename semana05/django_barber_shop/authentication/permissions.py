from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise AuthenticationFailed(detail={
                'message': 'Unauthorized'
            }, code=401)
        
        return True

class IsAdmin(BasePermission):
    def has_permission(self, request, view):      
        if request.user.role_id.name != 'ADMIN':
            raise AuthenticationFailed(detail={
                'message': 'Unauthorized'
            }, code=401)

        return True
    

class IsClient(BasePermission):
    def has_permission(self, request, view):
        if request.user.role_id.name != 'CLIENT':
            raise AuthenticationFailed(detail={
                'message': 'Unauthorized'
            }, code=401)

        return True
    

class IsClientOrAdmin(BasePermission):
    def has_permission(self, request, view):
        role = request.user.role_id.name
        if role == 'CLIENT' or role == 'ADMIN':
            return True
        
        raise AuthenticationFailed(detail={
            'message': 'Unauthorized'
        }, code=401)