from django.urls import path

from . import views



urlpatterns = [
	path('', views.core_home, name="core-home"),
	path('about/', views.core_about, name="core-about"),
]


