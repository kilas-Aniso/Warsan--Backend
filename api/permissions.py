from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to allow administrators full access,
    but read-only access for others (including Healthworkers and NGOs).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permission to allow administrators full access,
    object owners access, and read-only access for others.
    """
    def has_object_permission(self, request, view, obj):
        if request.user and (request.user.is_staff):
            return True
        return False

class IsAdminOrNGO(permissions.BasePermission):
    """
    Custom permission for administrators and NGOs (CustomUsers).
    """
    def has_object_permission(self, request, view, obj):
        print(f"::::::::::::::::::::::::::::::::::::{request.user}=============")
        if request.user and (request.user.is_staff):
            return True
        return False

class IsHealthworker(permissions.BasePermission):
    """
    Custom permission for Healthworkers.
    """
    def has_permission(self, request, view):
        return getattr(request.user, 'is_healthworker',True)

