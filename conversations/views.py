from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User


# Create your views here.
def LoginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        # else:
        #     messages.error(request, 'Invalid username or password')

    context={'page':page}
    return render(request, 'login-register.html', context)

def RegisterPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        
        else:
            messages.error(request, 'An error occurred during registration')
        
    context = {'form': form}
    return render(request,'login-register.html', context)

def LogoutPage(request):
    logout(request)
    return redirect('index')

def index(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(topic__name__icontains=q)
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'index.html', context)

@login_required(login_url='login')
def topic_detail(request, pk):
    topic = Topic.objects.get(id=pk)
    context = {'topic': topic}
    return render(request, 'topic_detail.html', context)

@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    conversations = room.conversation_set.all().order_by('-created_at')
    room_mates = room.room_mates.all()
    if request.method == 'POST':
        conversations = Conversation.objects.create(
            author = request.user,
            room = room,
            content = request.POST.get('content')
        )
        room.room_mates.add(request.user)
        return redirect('room', pk=room.id)


    context= {'room': room, 'conversations': conversations, 'room_mates': room_mates}
    return render(request, 'room.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    # PERMISSIONS
    if request.user  != room.host:
        return HttpResponse('Not allowed! Only the host can Update this room!')
    
    if request.method =='POST':
        form= RoomForm(request.POST, instance=room) 
    if form.is_valid():
            form.save()
            return redirect('index')
        
    context={'room': room, 'form': form}
    return render(request, 'room_form.html', context)

@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_comment(request, pk):
    conversation= Conversation.objects.get(id=pk)

    if request.user  != conversation.user:
        return HttpResponse('Not allowed! You cannot delete this conversation!')
    
    if request.method =='POST':
        conversation.delete()
        return redirect('index')
    return render(request, 'delete.html', {'object':conversation})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')