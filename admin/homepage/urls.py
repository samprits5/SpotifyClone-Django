from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='homepage-index'),
    path('edit/<int:id>/', views.edit, name='homepage-edit'),
    path('update/<int:id>/', views.update, name='homepage-update'),
]