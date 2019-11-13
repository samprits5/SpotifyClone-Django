from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='player-index'),
    path('<int:sid>/', views.index_id, name='player-index-id'),
    path('favorites/<int:sid>/', views.favorites_list, name='player-favorites'),
    path('addtofavorites/', views.favorites, name='player-favorites-add'),
]