from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='song-add'),
    path('save/', views.save, name='song-save'),
    path('index/', views.index, name='song-index'),
    path('delete/<int:id>/', views.delete, name='song-delete'),
    path('edit/<int:id>/', views.edit, name='song-edit'),
    path('update/<int:id>/', views.update, name='song-update'),
    path('details/<int:id>/', views.details, name='song-details'),
]