"""Sales views."""

# Django
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.db import transaction
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

# Django Views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Django Messages
from django.contrib.messages.views import SuccessMessageMixin

# Filters
from apps.sales.filters import SaleFilter

# Filters view
from utils.views.filters import FilteredListView

# Forms 
from apps.sales.forms import (
    ItemSaleInlineFormSet, 
    SaleForm
)

# Models
from apps.sales.models import (
    Customer, 
    Sale
)

# Views
from apps.utils.views_mixin import (
    ViewBaseMixin, 
    ViewListByStatusMixin
)

# Utils
from apps.utils.permissions import StaffRequiredMixin
from apps.utils.forms import CustomDateInput


class SaleListView(ViewListByStatusMixin, ListView):
    """Sale list view."""

    model = Sale
    paginate_by = 25

class SaleFilterListView(FilteredListView):
	"""Sale filter list view."""

	model = Sale
	paginate_by = 25
	filterset_class = SaleFilter

class SaleDetailView(DetailView):
    """Sale detail view."""

    model = Sale


@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class SaleCreateView(CreateView):
    """Sale create view."""

    model = Sale
    form_class = SaleForm
    success_url = None

    def get_context_data(self, **kwargs):
        context = super(SaleCreateView, self).get_context_data(**kwargs)
        
        if self.request.POST:
            context['item_sales'] = ItemSaleInlineFormSet(self.request.POST)
        else:
            context['item_sales'] = ItemSaleInlineFormSet()

        return context
        
    def form_valid(self, form):
        context = self.get_context_data()
        item_sales = context['item_sales']
        
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if item_sales.is_valid():
                item_sales.instance = self.object
                item_sales.save()
                
        return super(SaleCreateView, self).form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('sales:sales-update', kwargs={'pk': self.object.pk})
        

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class SaleUpdateView(UpdateView):
    """Sale update view."""

    model = Sale
    form_class = SaleForm
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(SaleUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['item_sales'] = ItemSaleInlineFormSet(self.request.POST, instance=self.object)
        else:
            context['item_sales'] = ItemSaleInlineFormSet(instance=self.object)
        return context
        
    def form_valid(self, form):
            context = self.get_context_data()
            item_sales = context['item_sales']
            with transaction.atomic():
                self.object = form.save()

                if item_sales.is_valid():
                    item_sales.instance = self.object
                    item_sales.save()
            return super(SaleUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('sales:sale-update', kwargs={'pk': self.object.pk})

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class SaleDelete(SuccessMessageMixin, DeleteView):
    """Sale delete."""

    model = Sale

    def get_success_url(self):
        return reverse_lazy('sales:sales') + "?remove"

