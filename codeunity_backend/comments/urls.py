from django.urls import path
from comments import views

urlpatterns = [
    path('chatroomcomments/', views.get_chatroom_comments),
    
    
]