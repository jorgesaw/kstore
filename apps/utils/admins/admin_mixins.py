"""Admin mixins."""


class ActiveModelSuperUserMixin:
    """Active model superuser mixin.

    Change active model only by superuser.
    """

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['active'].disabled = True

        return form