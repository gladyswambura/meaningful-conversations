from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    rooms = Room.objects.all()
    conversations = Conversation.objects.all()
    context = {'rooms': rooms, 'conversations': conversations}
    return render(request, 'index.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context= {'room': room}
    return render(request, 'room.html', context)