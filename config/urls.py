"""config URL Configuration"""

# Libraries
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Base Views
from .views import home_view

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('clients/', include(('src.clients.urls', 'clients'), namespace='clients')),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
