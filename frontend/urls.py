from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('signup/', views.signup, name='home-signup'),
    path('signup/post', views.signup_post, name='home-signup-post'),
    path('login/', views.login, name='home-login'),
    path('login/post', views.login_post, name='home-login-post'),
    path('logout/', views.logout_post, name='home-logout'),
    path('account/', include('frontend.account.urls')),
    path('webplayer/', include('frontend.webplayer.urls')),
]