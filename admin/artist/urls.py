from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='artist-add'),
    path('save/', views.save, name='artist-save'),
    path('index/', views.index, name='artist-index'),
    path('delete/<int:id>/', views.delete, name='artist-delete'),
    path('edit/<int:id>/', views.edit, name='artist-edit'),
    path('update/<int:id>/', views.update, name='artist-update'),
]