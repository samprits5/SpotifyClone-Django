from django.urls import path, include

urlpatterns = [
    path('', include('admin.login.urls')),
]