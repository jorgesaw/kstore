"""Inventories URLs."""

# Django
from django.urls import path, include

# Views
from .views import categories as categories_views
from .views import products as products_views
from .views import subcategories as subcategories_views


urlpatterns = [ 
    path('categories/', categories_views.CategoryListView.as_view(), name='categories'),
    path('categories/create/', categories_views.CategoryCreate.as_view(), name='category-create'),
    path('categories/<slug:slug_name>/', categories_views.CategoryDetailView.as_view(), name='category'),
    path('categories/update/<slug:slug_name>/', categories_views.CategoryUpdate.as_view(), name='category-update'),
    path('categories/delete/<slug:slug_name>/', categories_views.CategoryDelete.as_view(), name='category-delete'),

    path('subcategories/', subcategories_views.SubCategoryListView.as_view(), name='subcategories'),
    path('subcategories/create/', subcategories_views.SubCategoryCreate.as_view(), name='subcategory-create'),
    path('subcategories/<slug:slug_name>/', subcategories_views.SubCategoryDetailView.as_view(), name='subcategory'),
    path('subcategories/update/<slug:slug_name>/', subcategories_views.SubCategoryUpdate.as_view(), name='subcategory-update'),
    path('subcategories/delete/<slug:slug_name>/', subcategories_views.SubCategoryDelete.as_view(), name='subcategory-delete'), 
    
    path('products/', products_views.ProductListView.as_view(), name='products'),
    path('products/create/', products_views.ProductCreate.as_view(), name='product-create'),
    path('products/<slug:slug_name>/', products_views.ProductDetailView.as_view(), name='product'),
    path('products/update/<slug:slug_name>/', products_views.ProductUpdate.as_view(), name='product-update'),
    path('products/delete/<slug:slug_name>/', products_views.ProductDelete.as_view(), name='product-delete'), 
]
