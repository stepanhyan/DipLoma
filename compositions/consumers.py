# # compositions/consumers.py
#
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from .models import Songs
#
#
# @database_sync_to_async
# def get_user_profile(scope_user):
#     return scope_user.userprofile, False
#
#
# class LikeConsumer(AsyncWebsocketConsumer):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.song_group_name = None
#         self.song_id = None
#
#     async def connect(self):
#         await self.accept()
#         self.song_id = self.scope['url_route']['kwargs']['song_id']
#         self.song_group_name = f"song_{self.song_id}"
#
#         await self.channel_layer.group_add(
#             self.song_group_name,
#             self.channel_name
#         )
#
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.song_group_name,
#             self.channel_name
#         )
#         pass
#
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         action = text_data_json['action']
#         song_id = text_data_json['song_id']
#
#         if action == 'like':
#             await self.handle_like(song_id)
#         elif action == 'unlike':
#             await self.sync_remove_like()
#
#         await self.sync_send_like_count()
#
#     @database_sync_to_async
#     async def handle_like(self, song_id):
#         song = await Songs.objects.get(id=song_id)
#         user_profile, _ = await get_user_profile(self.scope['user'])
#
#         if not song.likes_users.filter(id=user_profile.id).exists():
#             song.likes_users.add(user_profile)
#         pass
#
#     async def sync_send_like_count(self):
#         song = await Songs.objects.get(id=self.song_id)
#         likes_count = await song.likes_users.count()
#
#         await self.channel_layer.group_send(
#             self.song_group_name,
#             {
#                 'type': 'like_count',
#                 'likes_count': likes_count
#             }
#         )
#
#     async def like_count(self, event):
#         likes_count = event['likes_count']
#
#         await self.send(text_data=json.dumps({
#             'likes_count': likes_count
#         }))
#
#     @database_sync_to_async
#     async def sync_add_like(self):
#         song = await Songs.objects.get(id=self.song_id)
#         user_profile, _ = await get_user_profile(self.scope['user'])
#
#         if not song.likes_users.filter(id=user_profile.id).exists():
#             song.likes_users.add(user_profile)
#
#     @database_sync_to_async
#     async def sync_remove_like(self):
#         song = await Songs.objects.get(id=self.song_id)
#         user_profile, _ = await get_user_profile(self.scope['user'])
#
#         if song.likes_users.filter(id=user_profile.id).exists():
#             song.likes_users.remove(user_profile)
