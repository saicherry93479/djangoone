"""
ASGI config for Remainder project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.urls import path
from django.core.asgi import get_asgi_application
from remainderone.consumers import ChatConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Remainder.settings')
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter([
            path("ws/chat/<str:room_name>/",ChatConsumer())
        ])
    )
})
