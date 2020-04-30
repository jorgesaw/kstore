"""Sales app URLs."""

# Django
from django.urls import path, include

# Views
from .views import customers as customers_views
from .views import sales as sales_views


urlpatterns = [ 
    path('customers/', customers_views.CustomerListView.as_view(), name='customers'),
    path('customers/create/', customers_views.CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/', customers_views.CustomerDetailView.as_view(), name='customer'),
    path('customers/update/<int:pk>/', customers_views.CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/delete/<int:pk>/', customers_views.CustomerDelete.as_view(), name='customer-delete'),
    
    path('sales/', sales_views.SaleListView.as_view(), name='sales'),
    path('sales/create/', sales_views.SaleCreateView.as_view(), name='sale-create'),
    path('sales/<int:pk>/', sales_views.SaleDetailView.as_view(), name='sale'),
    path('sales/update/<int:pk>/', sales_views.SaleUpdateView.as_view(), name='sale-update'),
    path('sales/delete/<int:pk>/', sales_views.SaleDelete.as_view(), name='sale-delete'),

]
