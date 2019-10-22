from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='favorite-index'),
    path('details/<int:id>/', views.details, name='favorite-details'),
]