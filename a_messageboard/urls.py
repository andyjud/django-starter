from django.urls import path
from .views import message_board_view


urlpatterns = [
    path("", message_board_view, name="message_board_index"),
]
