from typing import final

from django.apps import AppConfig


@final
class AccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "rtchat.apps.account"
