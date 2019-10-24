from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='player-index'),
    path('<int:sid>/', views.index_id, name='player-index-id'),
]