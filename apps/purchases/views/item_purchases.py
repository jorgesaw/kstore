"""Item purchases views."""

# Django
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.conf import settings

# Django views
from django.views.generic.edit import (
    CreateView, 
    UpdateView
)

# Messages
from django.contrib.messages.views import SuccessMessageMixin

# Forms 


# Models
from apps.purchases.models import (
    Supplier, 
    Purchase
)

# Views
from apps.utils.views_mixin import (
    ViewBaseMixin, 
    ViewListByStatusMixin
)

# Utils
from apps.utils.permissions import StaffRequiredMixin



    

