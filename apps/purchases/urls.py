"""Purchases app URLs."""

# Django
from django.urls import path, include

# Views
from .views import suppliers as suppliers_views
from .views import purchases as purchases_views


urlpatterns = [ 
    path('suppliers/', suppliers_views.SupplierListView.as_view(), name='suppliers'),
    path('suppliers/create/', suppliers_views.SupplierCreateView.as_view(), name='supplier-create'),
    path('suppliers/<int:pk>/', suppliers_views.SupplierDetailView.as_view(), name='supplier'),
    path('suppliers/update/<int:pk>/', suppliers_views.SupplierUpdateView.as_view(), name='supplier-update'),
    path('suppliers/delete/<int:pk>/', suppliers_views.SupplierDelete.as_view(), name='supplier-delete'),

    path('purchases/', purchases_views.PurchaseListView.as_view(), name='purchases'),
    path('purchases/create/', purchases_views.PurchaseCreateView.as_view(), name='purchase-create'),
    path('purchases/<int:pk>/', purchases_views.PurchaseDetailView.as_view(), name='purchase'),
    path('purchases/update/<int:pk>/', purchases_views.PurchaseUpdateView.as_view(), name='purchase-update'),
    path('purchases/delete/<int:pk>/', purchases_views.PurchaseDelete.as_view(), name='purchase-delete'),
]
