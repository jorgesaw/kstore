"""Inventories admin."""

# Django
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

# Django forms
from django import forms

# Actions Mixin
from apps.utils.admin.actions import ActionDownloadData

# Models
from apps.inventories.models import (
    Product, 
    Category,
    SubCategory,  
    ProductWithoutPrice, 
    PriceWithDesc, 
    ProductProxi,
    ProductWithoutPriceProxi
)

# Mixin
from apps.utils.admin import ActiveModelSuperUserMixin


@admin.register(Category)
class CategoryAdmin(ActionDownloadData, ActiveModelSuperUserMixin, admin.ModelAdmin):
    """Category admin."""

    fields = ('name', 'active', 'created', 'modified')
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'active')
    search_fields = ('name',)
    actions = ['download_data_csv',]


@admin.register(SubCategory)
class SubCategoryAdmin(ActionDownloadData, ActiveModelSuperUserMixin, admin.ModelAdmin):
    """Category admin."""

    autocomplete_fields = ('category',)
    fields = ('name', 'category', 'active', 'created', 'modified')
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'category', 'active')
    search_fields = ('name', 'category__name')
    actions = ['download_data_csv',]


@admin.register(PriceWithDesc)
class PriceAdmin(ActionDownloadData, admin.ModelAdmin):
    """Price admin.
    
    Precio que se utiliza a la hora de crear una venta como ítem de venta.
    Es conveniente en los casos en que un mismo producto puede aparecer varias veces
    con diferente descripción. Por ejemplo, un producto que tiene diferentes precios:

    * Precio con venta mayorista.
    * Precio con venta minorista.

    De esta forma se puede diferenciar dentro de la venta.
    """

    list_display = ('desc', 'value', 'product')
    ordering = ('id',)
    search_fields = ('desc', )
    extra = 1
    actions = ['download_data_csv',]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


class PriceTabularAdmin(admin.TabularInline):
    """Price tabular admin."""

    model = PriceWithDesc
    
    fields = ('desc', 'value')
    list_display = ('desc', 'value')
    ordering = ('id',)
    search_fields = ('desc', )
    extra = 1

"""
from django import forms
class PriceForm(forms.ModelForm):
    desc = forms.CharField()
    
    class Meta:
        ProductWithoutPrice
"""

@admin.register(Product)
class ProductAdmin(ActionDownloadData, ActiveModelSuperUserMixin, admin.ModelAdmin):
    """Product admin."""

    fieldsets = (
        (None, {
            'fields': ('active', 'code', 'barcode', 'name', 'subcategory', 'price', 'stock'),
        }),
        ('Datos extras', {
            'fields': ('desc', 'stock_min', 'stock_max', 'picture'),
        }),
    )
    autocomplete_fields = ('subcategory',)
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'code', 'barcode', 'subcategory_view')
    ordering = ('name', 'code')
    search_fields = ('code', 'barcode', 'name', 'desc', 'subcategory__name')
    date_hierarchy = 'modified' # Jerarquizar por fechas
    list_filter = ('subcategory__name', )
    actions = ['download_data_csv',]

    #form = PriceForm
    #inlines = [PriceTabularAdmin,]

    """
    def save_model(self, request, obj, form, change):
        # Salvar un atributo que solo aparece en el formulario admin.
        print(form.cleaned_data.get('desc', None))
        super().save_model(request, obj, form, change)
    """

    def subcategory_view(self, obj):
        link = reverse("admin:inventories_subcategory_change", args=[obj.subcategory.id])
        return format_html('<a href="{}">Editar {}</a>', link, obj.subcategory.name)
    subcategory_view.short_description = "Categoría"


class StockProductForm(forms.ModelForm):
    """Stock product form."""

    add_quantity = forms.IntegerField()
    
    class Meta:
        """Meta class."""

        Product


class StockProductWithoutForm(forms.ModelForm):
    """Stock product without form."""    

    add_quantity = forms.IntegerField()
    
    class Meta:
        """Meta class."""

        ProductWithoutPrice


@admin.register(ProductProxi)
class ProductStockAdmin(ProductAdmin):
    """Product stock admin."""

    form = StockProductForm
    readonly_fields = ('name', 'stock',)
    fieldsets = (
        (None, {
            'fields': ('name', 'stock', 'add_quantity'),
        }),
    )
    list_display = ('name', 'stock')
    search_fields = ('name', 'code', 'subcategory__name')
    list_filter = ('subcategory__name', )
    inlines = []

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True
    
    def save_model(self, request, obj, form, change):
        nueva_cant = form.cleaned_data.get('add_quantity', None)
        if obj.stock:
            obj.stock += nueva_cant
        else:
            obj.stock = nueva_cant
        super().save_model(request, obj, form, change)


@admin.register(ProductWithoutPriceProxi)
class ProductWithoutPriceStockAdmin(ProductStockAdmin):
    """Product without price stock admin."""    

    form = StockProductWithoutForm

