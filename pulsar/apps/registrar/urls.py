from django.urls import path

from . import views



urlpatterns = [
	path('register/', views.registrar_register, name="registrar-register"),
	path('login/', views.registrar_login, name="registrar-login"),
]
