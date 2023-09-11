# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_endpoint, name='info_endpoint'),
]
