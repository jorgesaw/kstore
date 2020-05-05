"""Customers views."""

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
from apps.sales.filters import CustomerFilter

# Filters view
from utils.views.filters import FilteredListView

# Forms 
from apps.sales.forms import CustomerForm 
from apps.persons.forms import (AddressInlineForm, AddressInlineUpdateForm)

# Models
from apps.sales.models import Customer

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


class CustomerListView(ViewListByStatusMixin, ListView):
    """Customer list view."""

    model = Customer
    paginate_by = 25

class CustomerFilterListViev(FilteredListView):
	"Customer filter list view."

	model = Customer
	paginate_by = 25
	filterset_class = CustomerFilter


class CustomerDetailView(DetailView):
    """Customer detail view."""

    model = Customer


@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class CustomerCreateView(SuccessMessageMixin, CreateWithInlinesView):
    """Customer create view."""

    model = Customer
    form_class = CustomerForm
    inlines = [AddressInlineForm, ]
    success_url = reverse_lazy('sales:customers')
    template_name = 'sales/customer_form.html'
    success_message = "Datos actualizados exitosamente." 


@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class CustomerUpdateView(SuccessMessageMixin, UpdateWithInlinesView):
    """Customer update view."""

    model = Customer
    form_class = CustomerForm
    inlines = [AddressInlineUpdateForm, ]
    template_name_suffix = "_update_form"
    success_message = "Datos actualizados exitosamente."

    def get_success_url(self):
        return reverse_lazy('sales:customer-update', args=[self.object.id]) + "?ok"

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class CustomerDelete(SuccessMessageMixin, DeleteView):
    """Customer delete."""

    model = Customer

    def get_success_url(self):
        return reverse_lazy('purchases:suppliers') + "?remove"

