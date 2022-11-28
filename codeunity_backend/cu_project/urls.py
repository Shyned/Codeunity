
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/user/', include ('user.urls')),
    path('api/chatroom/',include('chatroom.urls')),
    path('api/comments/',include('comments.urls')),
    ]
    
