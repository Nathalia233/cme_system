from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Permissão personalizada para administradores.
    """
    def has_permission(self, request, view):
        return request.user.role == 'Administrativo'

class IsNursing(permissions.BasePermission):
    """
    Permissão personalizada para o usuário de Enfermagem.
    """
    def has_permission(self, request, view):
        return request.user.role == 'Enfermagem'

class IsTechnical(permissions.BasePermission):
    """
    Permissão personalizada para o usuário Técnico.
    """
    def has_permission(self, request, view):
        return request.user.role == 'Técnico'