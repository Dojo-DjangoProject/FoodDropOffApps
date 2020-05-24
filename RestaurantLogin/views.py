from django.shortcuts import render, HttpResponse, redirect
from .models import Restaurant, RestaurantManager

def index(request):
    return render(request,'login_registration.html')

def create(request):
    Restaurant.objects.create(
        name = request.POST['name'],
        owner = request.POST['owner'],
        address = request.POST['address'],
        email_address = request.POST['email'],
        password = request.POST['pword']
    )
    return redirect('/')