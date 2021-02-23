"""
ASGI config for DeployASGI project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
'''
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DeployASGI.settings")

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from .routing import *


application = ProtocolTypeRouter({
    "http":get_asgi_application(),

    "websocket":AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
})
'''


import os

from django.core.asgi import get_asgi_application
from .routing import *
from channels.routing import ProtocolTypeRouter,URLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DeployASGI.settings")

application = ProtocolTypeRouter({
    "http":get_asgi_application(),

    "websocket":URLRouter(websocket_urlpatterns),
})