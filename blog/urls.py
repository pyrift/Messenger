from django.urls import path,include
from . import views  # yoki: from .views import chat_list, messag
urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('chats/<int:chat_id>/messages/', views.message, name='chat_messages'),
    path('update/<int:chat_id>/', views.update, name='update'),
    path('porofil/<int:chat_id>/', views.porofil, name='porofil'),
]
