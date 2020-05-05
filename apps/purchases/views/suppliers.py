"""Suppliers views."""

# Django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.conf import settings

# Messages
from django.contrib.messages.views import SuccessMessageMixin

# Filters
from apps.purchases.filters import SupplierFilter

# Filters view
from utils.views.filters import FilteredListView

# Forms 
from apps.purchases.forms import SupplierForm 
from apps.persons.forms import (AddressInlineForm, AddressInlineUpdateForm)

# Models
from apps.purchases.models import Supplier

# Views
from apps.utils.views_mixin import (
    ViewBaseMixin, 
    ViewListByStatusMixin
)

# Utils
from apps.utils.permissions import StaffRequiredMixin

# Extra views
from extra_views import ( 
            CreateWithInlinesView, 
            UpdateWithInlinesView, 
            InlineFormSetFactory,
)


class SupplierListView(FilteredListView):
    """Supplier list view."""

    model = Supplier
    paginate_by = 25
    filterset_class = SupplierFilter


class SupplierDetailView(DetailView):
    """Supplier detail view."""

    model = Supplier


@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class SupplierCreateView(SuccessMessageMixin, CreateWithInlinesView):
    """Supplier create view."""

    model = Supplier
    form_class = SupplierForm
    inlines = [AddressInlineForm, ]
    success_url = reverse_lazy('purchases:suppliers')
    template_name = 'purchases/supplier_form.html'
    success_message = "Datos actualizados exitosamente." 


@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class SupplierUpdateView(SuccessMessageMixin, UpdateWithInlinesView):
    """Supplier update view."""

    model = Supplier
    form_class = SupplierForm
    inlines = [AddressInlineUpdateForm, ]
    template_name_suffix = "_update_form"
    success_message = "Datos actualizados exitosamente."

    def get_success_url(self):
        return reverse_lazy('purchases:supplier-update', args=[self.object.id]) + "?ok"

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class SupplierDelete(SuccessMessageMixin, DeleteView):
    """Supplier delete."""

    model = Supplier
    success_url = reverse_lazy('purchases:suppliers')

    def get_success_url(self):
        return reverse_lazy('purchases:suppliers') + "?remove"

