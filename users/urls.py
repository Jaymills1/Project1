from django.urls import path, include
from . import views


urlpatterns = [
    path('users/', views.userPage, name= 'user-page'),
    path('details/<int:pk>', views.details, name= 'details-page'),
]