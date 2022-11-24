from django.urls import path
from chatroom import views

urlpatterns = [
    path('openchatrooms/', views.get_all_chatrooms),
    
]