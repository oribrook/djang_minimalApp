from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat', views.chat),
    path('rooms', views.serve_chat_rooms),  # show available rooms
    path('send_to_rooms', views.send_to_rooms),  
]
