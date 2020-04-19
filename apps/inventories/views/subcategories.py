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

# Messages
from django.contrib.messages.views import SuccessMessageMixin

# Forms 
from apps.inventories.forms import SubCategoryForm

# Models
from apps.inventories.models import SubCategory

# Views
from apps.utils.views_mixin import (
    ViewBaseMixin, 
    ViewListByStatusMixin
)


class SubCategoryListView(ViewListByStatusMixin, ListView):
    """Subcategory list view."""

    model = SubCategory
    paginate_by = 25

class SubCategoryDetailView(ViewBaseMixin, DetailView):
    """Subcategory detail view."""

    model = SubCategory

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class SubCategoryCreate(SuccessMessageMixin, CreateView):
    """Subcategory create."""

    model = SubCategory
    form_class = SubCategoryForm
    success_url = reverse_lazy('inventories:subcategories')
    success_message = "Datos creados exitosamente."

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class SubCategoryUpdate(ViewBaseMixin, SuccessMessageMixin, UpdateView):
    """Subcategory update."""

    model = SubCategory
    form_class = SubCategoryForm
    template_name_suffix = "_update_form"
    success_message = "Datos actualizados exitosamente."

    def get_success_url(self):
        return reverse_lazy('inventories:subcategory-update', args=[self.object.slug_name]) + "?ok"

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class SubCategoryDelete(ViewBaseMixin, SuccessMessageMixin, DeleteView):
    """Subcategory delete."""

    model = SubCategory
    success_url = reverse_lazy('products:categories')
    success_message = "Datos eliminados exitosamente."

    def get_success_url(self):
        return reverse_lazy('inventories:subcategories') + "?remove"
