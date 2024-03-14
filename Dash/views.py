from django.shortcuts import render, redirect
from .models import Users, Room, Message, Users_Rooms
from django.http import HttpResponse, JsonResponse
from datetime import datetime

# Create your views here.

def login(request):
    return render(request, 'login.html')

def index(request, pk):
    global pic
    user_details = Users.objects.get(user=pk)
    name = user_details.name
    pic = user_details.pic

    return render(request, 'index.html', {'user_details': user_details, 'user': pk , 'name': name, 'pic': pic})





def register(request):
    
    return render(request, 'signup.html')

def checkUser(request):
    password = request.POST.get('password')
    username = request.POST.get('username')

    if Users.objects.filter(user=username).exists():
        if Users.objects.filter(password= password).exists():
            print('is a user')
            return redirect('/dashboard/'+username)
            return HttpResponse('loged in succesfully')
        else:
            print('not an user')
            return HttpResponse('not an user')
            
    else:
        print('not an user')
        return HttpResponse('not an user')
    
    

def signup(request):
     username = request.POST.get('Newusername')
     name = request.POST.get('Newname')
     password = request.POST.get('Newpassword')

     

     newUser = Users.objects.create(user = username, name =name, password = password)
     newUser.save()

    #  return redirect('/'+username)
     return redirect('/dashboard/'+username)
     return HttpResponse('user saved succesfully')
    
    # return redirect('/'+user)

    # return render(request, 'signup.html')


def chat_index(request, pk):
    user_details = Users.objects.get(user=pk)
    

    return render(request, 'chat_index.html', {'user_details': user_details, 'user': pk, 'room': room})



def checkview(request, pk):
    room = request.POST.get('room')
    user_details = Users.objects.get(user=pk)

    user_rooms = Users_Rooms.objects.all().values()
    user_rooms = user_rooms.filter(users_id = user_details.id)
    user_rooms_names = []

    for chat in user_rooms:
        name = Room.objects.get(id=chat['rooms_id'])
        user_rooms_names.append(name.room_name)

    room = user_rooms_names[0]
    print(room)
    room_details = Room.objects.get(room_name = room)

    

    if Room.objects.filter(room_name=room).exists():

        if Users_Rooms.objects.filter( users_id = user_details.id, rooms_id = room_details.id).exists():
            pass
        else:
            user_rooms = Users_Rooms.objects.create(users_id = user_details.id, rooms_id = room_details.id)
            user_rooms.save()
        
        return redirect(room+ '/')
    
    else:
        
        new_room = Room.objects.create(room_name = room)
        new_room.save()
        if Users_Rooms.objects.filter( users_id = user_details.id, rooms_id = new_room.id).exists():
            pass
        else:
            user_rooms = Users_Rooms.objects.create(users_id = user_details.id, rooms_id = new_room.id)
            user_rooms.save()

        print('no')
        return redirect(room +'/')
        

def room(request, room, pk):
     global user_details
     user_details = Users.objects.get(user=pk)

     user_rooms = Users_Rooms.objects.all().values()
     user_rooms = user_rooms.filter(users_id = user_details.id)
     user_rooms_names = []
     last_text = []
     for chat in user_rooms:
        name = Room.objects.get(id=chat['rooms_id'])
        user_rooms_names.append(name.room_name)



     username = request.GET.get('username')
     room_details = Room.objects.get(room_name=room)
     
    #  user_rooms = Users_Rooms.objects.get(users_id = user_details.id)
    #  print(user_rooms)
    

     

     return render(request, 'room.html', {'room': room, 'room_details':room_details,'user_details':user_details, 'user': pk, 'username': username, 'users_rooms': user_rooms_names})

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message send succesfully')

def getMessages(request, room):
    global user_details
    room_details =  Room.objects.get(room_name = room)
    messages = list(Message.objects.filter(room= room_details.id).values())
    
    
    text = Message.objects.all().values()
    for i in messages:
        
        hora= datetime.time(i['date']).strftime("%H:%M:%S")
        fecha = datetime.date(i['date'])
        i['hora']= hora
        i['fecha']= fecha
        
    
    
    username = user_details.user

    
    return JsonResponse({'messages': messages,'user': username, 'hora': hora, 'date':fecha})


