from django.contrib import admin
from django.urls import path, include


django_urls = [
    path('admin/', admin.site.urls),
]

third_party_urls = [
    
]

pulsar_urls = [
    path('', include('core.urls')),
    path('', include('account.urls')),
]


urlpatterns = django_urls + pulsar_urls + third_party_urls