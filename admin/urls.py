from django.urls import path, include

urlpatterns = [
    path('', include('admin.login.urls')),
    path('dashboard/', include('admin.dashboard.urls')),
    path('genre/', include('admin.genre.urls')),
]