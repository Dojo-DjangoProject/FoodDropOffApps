from django.shortcuts import render, HttpResponse, redirect
from RestaurantEvent.models import Event
from .models import User
import bcrypt

def index(request):
    return HttpResponse('Works')
<<<<<<< HEAD
    
def user_info(request,user_id):
    return render(request,'user_welcome.html')
=======

def register(request):
    return render(request,'user_registration.html')

def create(request):
    # errors = User.objects.basic_validator(request.POST)

    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request,value)
    #     return redirect('/')
    # else:

        password_encoded = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'], 
            # birthday = request.POST['bday'],
            email = request.POST['email'],
            password = password_encoded,
            phone_number = request.POST['phone_number']
        )
        # request.session['user_email'] = request.POST['email']
        # request.session['fname'] = request.POST['fname']

        return HttpResponse('Registered')

def users(request):
    return render(request,'user_login.html')
    
def user_info(request,user_id):
    context = {
        'events' : Event.objects.all()
    }
    return render(request,'user_welcome.html',context)
>>>>>>> 99ec5774cbaff5f9d8ed7e3abd64d640c985ffc4
