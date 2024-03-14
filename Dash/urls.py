from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('signup', views.signup, name='signup'),
    path('checkUser', views.checkUser, name='checkUser'),
    path('dashboard/<str:pk>/', views.index, name='index'),
    # path('dashboard/<str:pk>/chat_index/', views.chat_index, name='chat_index'),

    path('dashboard/<str:pk>/checkview/', views.checkview, name='checkview/'),
    path('dashboard/<str:pk>/checkview/<str:room>/', views.room, name='room'),
    
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    
    
]