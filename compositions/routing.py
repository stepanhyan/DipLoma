# # routing.py
#
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from .consumers import LikeConsumer
#
# application = ProtocolTypeRouter(
#     {
#         "websocket": URLRouter(
#             [
#                 path("ws/songs/<int:song_id>/", LikeConsumer.as_asgi()),
#             ]
#         ),
#     }
# )
