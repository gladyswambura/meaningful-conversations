from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path ('room/<str:pk>/', views.room, name='room'),
    path('topic_detail/<str:pk>/', views.topic_detail, name='topic_detail'),
    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<str:pk>/', views.update_room, name='update_room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete_room'),
    path('delete_comment/<str:pk>/', views.delete_comment, name='delete_comment'),

    path('login/', views.LoginPage, name='login'),
    path('register/', views.RegisterPage, name='register'),
    path('logout/', views.LogoutPage, name='logout'),
]