from . import views
from django.urls import path

urlpatterns = [
    path('', views.greetings, name ='greetings'),
    path('filter/', views.filterlist, name='filter'),
    path('create/', views.create, name ='create'),
    path('detail/<int:id>', views.detail, name ='detail'),
    path('update/<int:id>', views.update, name ='update'),
    path('mark/<int:id>', views.mark, name ='marks'),
    path('exportcsv/', views.exportcsv, name ='exportcsv'),
    path('notification/', views.notification, name ='notification'),


]