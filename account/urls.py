from django.urls import path, include
from . import views

urlpatterns = [
    path('registeration/', views.register, name="register"),
    path('login/', views.loginUser, name="loginUser"),
    path('logout/', views.logoutUser, name="logoutUser"),
]