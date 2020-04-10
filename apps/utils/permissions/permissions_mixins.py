"""Permissions mixin."""

# Django
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

# Permissions
from django.contrib.admin.views.decorators import staff_member_required

class StaffRequiredMixin(object):
    """Staff required mixin.
    
    Required user is member of staff.
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect( reverse_lazy('admin:login') )
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)