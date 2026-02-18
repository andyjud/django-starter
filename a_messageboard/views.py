import threading

from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from a_messageboard.models import MessageBoard, Message
from a_messageboard.forms import MessageCreateForm


@login_required
def message_board_view(request):
    message_board = get_object_or_404(MessageBoard, id=1)
    form = MessageCreateForm()
    user = request.user

    if request.method == "POST":
        # Ensure user is subscribed to the message board
        if user in message_board.subscribers.all():
            form = MessageCreateForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.author = user
                message.message_board = message_board
                message.save()
                send_message_to_users(message)
        else:
            messages.warning(request, "You need to be subscribed! ⚠")
        return redirect("message_board_index")

    context = {"message_board": message_board, "form": form}
    return render(request, "message_board/index.html", context)


@login_required
def subscribe_view(request):
    board = get_object_or_404(MessageBoard, id=1)
    user = request.user

    # Subscribe user if he/she is not subscribed.
    if user not in board.subscribers.all():
        board.subscribers.add(user)
    else:
        board.subscribers.remove(user)

    return redirect("message_board_index")


def send_message_to_users(message: Message):
    board = message.message_board
    subscribers = board.subscribers.all()
    author = message.author.profile.name
    subject = f"New message from {author}"
    body = f"{author}: {message.body}\n\nRegards from\nMy Message Board 📩"

    def send_email_thread(subject_, body_, subscriber_):
        email = EmailMessage(subject_, body_, to=[subscriber_.email])
        email.send()

    for subscriber in subscribers:
        email_thread = threading.Thread(target=send_email_thread, args=(subject, body, subscriber))
        email_thread.start()
