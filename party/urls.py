from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('error404', views.home, name='error404'),
]
