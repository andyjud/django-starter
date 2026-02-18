from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def message_board_view(request):
    return render(request, "message_board/index.html")
