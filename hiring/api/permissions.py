from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):

    def has_permission(self, request, *args, **kwargs):
       def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True

            return obj.company.owner == request.user


class isSuperAdminUser(permissions.BasePermission):
    
    def has_permission(self, request, *args, **kwargs):
       def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user.is_superuser