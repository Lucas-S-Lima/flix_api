from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_perm(self, request, view):

        model_permission_codename = self.__get_model_permission_codename(
            method=request.method, view=view
        )

        if model_permission_codename:
            return request.user.has_perm(model_permission_codename)
        else:
            return False

    def __get_model_permission_codename(self, method, view):

        try:
            model_name = view.queryset.model._meta.model_name
            app_name = view.queryset.model._meta.app_labbel
            action = self.__get_action_sufix(method)

            return f'{app_name}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_action_sufix(self, method):

        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }

        return method_actions.get(method, '')
