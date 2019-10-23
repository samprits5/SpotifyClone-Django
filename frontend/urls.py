from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('signup/', views.signup, name='home-signup'),
    path('signup/post', views.signup_post, name='home-signup-post'),
]