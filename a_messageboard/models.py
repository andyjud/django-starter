from django.db import models
from django.contrib.auth.models import User

from a_home.models import BaseModel


class MessageBoard(models.Model):
    subscribers = models.ManyToManyField(User, related_name="message_board", blank=True)  # noqa:E501

    def __str__(self):
        return str(self.id)


class Message(BaseModel):
    message_board = models.ForeignKey(
        MessageBoard,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")  # noqa:E501
    body = models.TextField(max_length=2000)

    def __str__(self):
        return self.author.username
