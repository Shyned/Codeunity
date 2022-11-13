from django.urls import path
from chatroom import views

urlpatterns = [
    path('getchatrooms/', views.get_chatrooms),
]