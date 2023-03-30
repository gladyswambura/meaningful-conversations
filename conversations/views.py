from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'index.html', context)

def room(request, pk):
    conversations = Conversation.objects.all()
    room = Room.objects.get(id=pk)
    context= {'room': room, 'conversations': conversations}
    return render(request, 'room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method =='POST':
        #<!--add data to the form -->
        form= RoomForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('index')
        
    context={'form': form}
    return render(request, 'room_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method =='POST':
        form= RoomForm(request.POST, instance=room) 
    if form.is_valid():
            form.save()
            return redirect('index')
        
    context={'room': room, 'form': form}
    return render(request, 'room_form.html', context)

def delete_room(request, pk):
    room= Room.objects.get(id=pk)
    if request.method =='POST':
        room.delete()
        return redirect('index')
    return render(request, 'delete.html', {'object':room})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')