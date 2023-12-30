# chatapp/views.py
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


def index(request):
    return render(request, "index.html")

def room(request, room_name):
    messages = Message.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():            
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('chat_room', room_name=room_name)
    else:
        form = MessageForm()

    return render(request, 'room.html', {'room_name': room_name, 'messages': messages, 'form': form, 'user': request.user})