"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    
    # Core app
    path('', include(('apps.core.urls', 'core'), namespace='core')),

    path('', include(('apps.users.urls', 'users'), namespace='users')),
    
    # Auth
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include(('apps.registration.urls', 'registration'), namespace='registration')),

    # Profiles
    path('profiles/', include(('apps.profiles.urls', 'profiles'), namespace='profiles')),

    # Inventories
    path('inventories/', include(('apps.inventories.urls', 'inventories'), namespace='inventories')), 

    # Purchases
    path('purchases/', include(('apps.purchases.urls', 'purchases'), namespace='purchases')),
    
    # Sales
    path('sales/', include(('apps.sales.urls', 'sales'), namespace='sales')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

