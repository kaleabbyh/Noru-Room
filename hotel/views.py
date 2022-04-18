from django.shortcuts import redirect, render
from .form import RoomForm
from django.db.models import Q
from .models import *

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def loginpage(request):
    page = "login"
    errormessage = ''
    if request.user.is_authenticated:
        redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            # messages.error(request, 'user doesnt exist')
            errormessage = 'user doesnt exist'

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # messages.error(request, 'username or password doesnt exist')
            errormessage = 'username or password doesnt exist'

    context = {'page': page, 'errormessage': errormessage}
    return render(request,"hotel/customer/login.html", context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    # form = UserCreationForm()
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = user.username.lower()
    #         user.save()
    #         login(request, user)
    #         return redirect("home")
    #     else:
    #         messages.error(request, "error during registration")

    return render(request, 'hotel/customer/customer_register.html')



def homepage(request):
    return render(request, 'hotel/customer/index.html')


def home(request):
    
    rooms = room.objects.all()
    context = {'rooms':rooms}
    return render(request,"hotel/customer/home.html",context)


def book(request):
    Search = request.GET.get('Search') if request.GET.get('Search') != None else ''
    rooms = room.objects.filter(
        Q(room_category__room_category_name__contains=Search) |
        Q(room_category__room_category_name__contains=Search) 
        )
    
    room_categorys=room_category.objects.all()
    context = {'rooms':rooms,'room_categorys':room_categorys}
    return render(request,"hotel/customer/book.html",context)

def details(request,pk):
    roomm = room.objects.get(room_id=pk)
    roomm_messages = roomm.message_set.all().order_by('-created')[0:5]
    if request.method == "POST":
        messages = message.objects.create(
            user=request.user,
            room=roomm,
            body=request.POST.get('body')
        )
        return redirect('details', pk=roomm.room_id)
    context = {'room': roomm, 'room_messages': roomm_messages}
    return render(request,"hotel/customer/details.html",context)


def checkout(request):
    return render(request,"hotel/customer/checkout.html")


@login_required(login_url='login')
def add_room(request):
    places=place.objects.all()
    room_categorys=room_category.objects.all()
    room_operation="add room"
    form = RoomForm()
    if request.method == 'POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('error')
           
    context = {'places':places,'room_categorys':room_categorys,'form': form,'room_operation':room_operation}
    return render(request,"hotel/adminArea/room_form.html",context)

#update room
@login_required(login_url='login')
def update_room(request, pk):
    room_operation="update room"
    rooms = room.objects.get(room_id=pk)
    places=place.objects.all()
    room_categorys=room_category.objects.all()
    # form = RoomForm(instance=room)
    if request.method == 'POST':
        rooms.place.place_name = request.POST.get('place_name')
        rooms.room_category.room_category_name = request.POST.get('place_name')
        rooms.room_price = request.POST.get('room_price')
        rooms.room_number = request.POST.get('room_number')
        rooms.room_name = request.POST.get('room_name')
        rooms.romm_description = request.POST.get('romm_description')
        rooms.room_id = request.POST.get('room_id')
        rooms.room_image = request.POST.get('room_image')
        
        rooms.save()
        return redirect('home')
    context = {'rooms': rooms,'room_operation':room_operation,'places':places,'room_categorys':room_categorys}
    return render(request, 'hotel/adminArea/room_form.html',context)


@login_required(login_url='login')
def delete_room(request, pk):
    roomm = room.objects.get(room_id=pk)
    if request.method == "POST":
        roomm.delete()
        return redirect('home')
    context = {'obj': roomm}
    return render(request, 'hotel/adminArea/delete_room.html', context)


def delete_message(request, pk):
    messagee = message.objects.get(message_id=pk)

    if 1:
        messagee.delete()
        return redirect('details', pk=messagee.room.room_id)
    context = {'obj': messagee}
    return render(request,"hotel/customer/details.html",context)