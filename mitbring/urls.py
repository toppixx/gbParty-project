from django.urls import path, include
from . import views

urlpatterns = [
    path('mitbring', views.mitbring, name='mitbring'),

]
