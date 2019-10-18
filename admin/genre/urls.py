from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='genre-add'),
    path('save/', views.save, name='genre-save'),
    path('index/', views.index, name='genre-index'),
    path('delete/<int:id>/', views.delete, name='genre-delete'),
    path('edit/<int:id>/', views.edit, name='genre-edit'),
    path('update/<int:id>/', views.update, name='genre-update'),
]