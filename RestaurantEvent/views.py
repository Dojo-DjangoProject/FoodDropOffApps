from django.shortcuts import render, HttpResponse, redirect
from .models import Restaurant, RestaurantManager, Event

def index(request):

    # Sort by most recent day
    context = {
        'events' : Event.objects.all()
    }
    return render(request,'events.html',context)

def create(request):
    Event.objects.create(
        name=request.POST['name'],
        location=request.POST['location'],
        date=request.POST['date'],
        time=request.POST['time'],
        spots_available=request.POST['spots']
    )
    return redirect('/restaurant_event')