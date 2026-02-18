from django.urls import path
from .views import message_board_view, subscribe_view


urlpatterns = [
    path("", message_board_view, name="message_board_index"),
    path("subscribe/", subscribe_view, name="subscribe_view"),
    # path("unsubscribe/", unsubscribe_view, name="unsubscribe_view"),
]
