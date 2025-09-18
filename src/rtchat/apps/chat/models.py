from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=32)

    @property
    def group_name(self) -> str:
        return f"chat_room_{self.name}"


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now_add=True)
