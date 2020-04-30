"""Purchases views."""

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

# Forms 
from apps.purchases.forms import (
    ItemPurchaseInlineFormSet, 
    PurchaseForm
)

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
from apps.utils.forms import CustomDateInput


class PurchaseListView(ViewListByStatusMixin, ListView):
    """Purchase list view."""

    model = Purchase
    paginate_by = 25


class PurchaseDetailView(DetailView):
    """Purchase detail view."""

    model = Purchase


@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class PurchaseCreateView(CreateView):
    """Purchase create view."""

    model = Purchase
    form_class = PurchaseForm
    success_url = None

    def get_context_data(self, **kwargs):
        context = super(PurchaseCreateView, self).get_context_data(**kwargs)
        
        if self.request.POST:
            context['item_purchases'] = ItemPurchaseInlineFormSet(self.request.POST)
        else:
            context['item_purchases'] = ItemPurchaseInlineFormSet()

        return context
        
    def form_valid(self, form):
        context = self.get_context_data()
        item_purchases = context['item_purchases']
        
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if item_purchases.is_valid():
                item_purchases.instance = self.object
                item_purchases.save()
                
        return super(PurchaseCreateView, self).form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('purchases:purchase-update', kwargs={'pk': self.object.pk})
        

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class PurchaseUpdateView(UpdateView):
    """Purchase update view."""

    model = Purchase
    form_class = PurchaseForm
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(PurchaseUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['item_purchases'] = ItemPurchaseInlineFormSet(self.request.POST, instance=self.object)
        else:
            context['item_purchases'] = ItemPurchaseInlineFormSet(instance=self.object)
        return context
        
    def form_valid(self, form):
            context = self.get_context_data()
            item_purchases = context['item_purchases']
            with transaction.atomic():
                self.object = form.save()

                if item_purchases.is_valid():
                    item_purchases.instance = self.object
                    item_purchases.save()
            return super(PurchaseUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('purchases:purchase-update', kwargs={'pk': self.object.pk})

@method_decorator(staff_member_required(login_url=settings.LOGIN_URL), name='dispatch')
class PurchaseDelete(SuccessMessageMixin, DeleteView):
    """Purchase delete."""

    model = Purchase
    success_url = reverse_lazy('purchases:purchases')

    def get_success_url(self):
        return reverse_lazy('purchases:purchases') + "?remove"

