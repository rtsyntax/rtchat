import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from rtchat.apps.chat.models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]

        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room, _ = await database_sync_to_async(Room.objects.get_or_create)(
            name=room_name
        )

        # Join room group
        await self.channel_layer.group_add(self.room.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text = text_data_json["message"]

        message = Message(room=self.room, sender=self.user, text=text)
        await database_sync_to_async(message.save)()

        await self.channel_layer.group_send(
            self.room.group_name,
            {
                "type": "chat.message",
                "message": {"sender": self.user.username, "text": text},
            },
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
