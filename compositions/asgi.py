# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from compositions.routing import application
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'songs_store.settings')
#
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             application
#         )
#     ),
# })
