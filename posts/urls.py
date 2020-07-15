from django.urls import path, include
from . import views

urlpatterns = [
    path('post/<int:id>/', views.blogPost, name="blogPost"),
    path('addpost/>', views.addPost, name="addPost"),
    path('editpost/<int:id>/', views.editPost, name="editPost"),
    path('search/', views.search, name="search"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('', views.blogs, name="blogs"),
]