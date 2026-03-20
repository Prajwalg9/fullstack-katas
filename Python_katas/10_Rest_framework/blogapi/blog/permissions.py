from rest_framework import permissions

class IsPostProcessor(permissions.BasePermission):
    """
    Custom permission to only allow creators of a post to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the creator of the post.
        return obj.created_by == request.user