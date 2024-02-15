from rest_framework import permissions


# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)  # Check user is staff or not
        return is_admin or request.method in permissions.SAFE_METHODS
        # return True if user is Staff and permissions is in SAFE_METHODS
