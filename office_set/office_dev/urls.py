from . import views
from django.urls import path

urlpatterns = [
    path('Документы/', views.list, name='list'),
    ]