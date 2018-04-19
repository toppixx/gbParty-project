from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('dieparty', views.dieparty, name='dieparty'),
    path('error404', views.error404, name='error404'),
]
