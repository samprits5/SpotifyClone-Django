from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('login/', views.login, name='login-check'),
    path('dashboard/', include('admin.dashboard.urls')),
    path('logout/', views.logout_view, name='logout'),
]