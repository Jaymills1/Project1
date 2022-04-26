from django.urls import path
from . import views
from dashboard.urls import urlpatterns


urlpatterns = [
    path('signUp/', views.signUp, name= 'account-signUp'),
    path('', views.index, name= 'index-page'),
    path('login/', views.logIn, name= 'login'),
    path('logOut/', views.logIn, name= 'account-logOut'),
]
