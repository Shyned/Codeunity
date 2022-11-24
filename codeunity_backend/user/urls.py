from django.urls import path
from user import views

urlpatterns = [
    path('getuser/<pk>/', views.get_user),
    path('adduser/', views.add_user),
]