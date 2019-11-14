from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='player-index'),
    path('<int:sid>/', views.index_id, name='player-index-id'),

    path('favorites/<int:sid>/', views.favorites_list, name='player-favorites'),

    path('artist/<int:sid>/', views.artist, name='player-artist'),
    path('artist/songs/<int:sid>/<int:aid>', views.artist_details, name='player-artist-details'),

    path('mood/<int:sid>/', views.mood, name='player-mood'),
    path('mood/songs/<int:sid>/<int:mid>', views.mood_details, name='player-mood-details'),

    path('genre/<int:sid>/', views.genre, name='player-genre'),
    path('genre/songs/<int:sid>/<int:gid>', views.genre_details, name='player-genre-details'),

    path('category/<int:sid>/', views.category, name='player-category'),

    path('library/<int:sid>/', views.library, name='player-library'),

    path('search/<int:sid>/', views.search, name='player-search'),

    path('addtofavorites/', views.favorites, name='player-favorites-add'),
]