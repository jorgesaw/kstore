"""Categories views."""

# Django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.shortcuts import get_object_or_404

# Messages
from django.contrib.messages.views import SuccessMessageMixin

# Filters
from apps.inventories.filters import CategoryFilter

# Filters view
from utils.views.filters import FilteredListView

# Forms 
from apps.inventories.forms import CategoryForm

# Models
from apps.inventories.models import Category

# Views
from apps.utils.views_mixin import (
    ViewBaseMixin, 
    ViewListByStatusMixin
) 


class CategoryListView(FilteredListView):
    """Category list view."""

    model = Category
    paginate_by = 25
    filterset_class = CategoryFilter

class CategoryDetailView(ViewBaseMixin, DetailView):
    """Category detail view."""

    model = Category


@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class CategoryCreate(SuccessMessageMixin, CreateView):
    """Category create."""

    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('inventories:categories')
    success_message = "Datos creados exitosamente."

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class CategoryUpdate(ViewBaseMixin, SuccessMessageMixin, UpdateView):
    """Category update."""

    model = Category
    form_class = CategoryForm
    template_name_suffix = "_update_form"
    success_message = "Datos actualizados exitosamente."

    def get_success_url(self):
        return reverse_lazy('inventories:category-update', args=[self.object.slug_name]) + "?ok"

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class CategoryDelete(ViewBaseMixin, SuccessMessageMixin, DeleteView):
    """Category delete."""

    model = Category
    success_url = reverse_lazy('inventories:categories')
    success_message = "Datos eliminados exitosamente."

    def get_success_url(self):
        return reverse_lazy('inventories:categories') + "?remove"
