"""Products views."""

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

# Forms 
from apps.inventories.forms import ProductForm, CategoryForm, ProductWithoutPriceForm

# Models
from apps.inventories.models import Product, ProductWithoutPrice

# Views
from apps.utils.views_mixin import (
    ViewBaseMixin, 
    ViewListByStatusMixin
)

# Utils
from apps.utils.permissions import StaffRequiredMixin


class ProductListView(ViewListByStatusMixin, ListView):
    """Product list view."""

    model = Product
    paginate_by = 25

class ProductDetailView(ViewBaseMixin, DetailView):
    """Product detail view."""

    model = Product

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class ProductCreate(SuccessMessageMixin, CreateView):
    """Product create."""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('inventories:products')
    success_message = "Datos creados exitosamente."

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class ProductUpdate(ViewBaseMixin, SuccessMessageMixin, UpdateView):
    """Product update."""

    model = Product
    form_class = ProductForm
    template_name_suffix = "_update_form"
    success_message = "Datos actualizados exitosamente."

    def get_success_url(self):
        return reverse_lazy('inventories:product-update', args=[self.object.slug_name]) + "?ok"

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class ProductDelete(ViewBaseMixin, SuccessMessageMixin, DeleteView):
    """Product delete."""

    model = Product
    success_url = reverse_lazy('inventories:products')

    def get_success_url(self):
        return reverse_lazy('inventories:products') + "?remove"

