from django.urls import path
from . import consumers

""" here we define a routing between the asgi requests to consumers """

websocket_urlpatterns = [    
    path("ws", consumers.MyConsumer.as_asgi()),    
]