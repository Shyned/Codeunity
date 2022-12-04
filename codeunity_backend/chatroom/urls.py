from django.urls import path
from chatroom import views

urlpatterns = [
    path('openchatrooms/', views.get_all_chatrooms),
    path('selectedroom/<pk>/', views.get_chatroom),
    path('makeroom/', views.create_chat_room),
    path('deletechatroom/', views.delete_chatroom),
    
    
]