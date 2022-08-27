from django.contrib import admin
from django.urls import path, include


# URLS

django_urls = [
    path('admin/', admin.site.urls),
]

third_party_urls = [
    #path('api/', include('rest_framework.urls')),
]

pulsar_urls = [
    path('', include('core.urls')),
    path('', include('registrar.urls')),
]



urlpatterns = django_urls + pulsar_urls + third_party_urls


# ERRORS

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.error'
handler403 = 'core.views.permission_denied'
handler400 = 'core.views.bad_request'