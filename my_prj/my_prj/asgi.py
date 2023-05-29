import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import my_app.ws_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_prj.settings')


# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': 
        URLRouter(
            my_app.ws_routing.websocket_urlpatterns)
        
})