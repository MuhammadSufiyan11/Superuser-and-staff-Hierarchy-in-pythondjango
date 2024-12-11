from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('home/', views.user_home, name='user_home'),
    path('register/', views.register_user, name='register_user'),
]
