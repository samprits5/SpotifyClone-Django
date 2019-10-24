from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='account-index'),
    path('edit-profile', views.edit, name='account-edit'),
    path('update-profile', views.update, name='account-update'),
]