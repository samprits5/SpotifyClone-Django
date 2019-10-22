from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='user-index'),
    path('details/<int:id>/', views.details, name='user-details'),
]