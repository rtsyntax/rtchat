from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from rtchat.apps.chat.models import Room


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html")


@login_required
def room(request: HttpRequest, room_name: str) -> HttpResponse:
    room, _created = Room.objects.get_or_create(name=room_name)
    messages = room.message_set.order_by("timestamp").all()
    return render(
        request,
        "chat/room.html",
        {"room_name": room_name, "messages": messages},
    )
