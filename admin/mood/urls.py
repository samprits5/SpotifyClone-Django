from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='mood-add'),
    path('save/', views.save, name='mood-save'),
    path('index/', views.index, name='mood-index'),
    path('delete/<int:id>/', views.delete, name='mood-delete'),
    path('edit/<int:id>/', views.edit, name='mood-edit'),
    path('update/<int:id>/', views.update, name='mood-update'),
]