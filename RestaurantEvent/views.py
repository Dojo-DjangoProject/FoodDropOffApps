from django.shortcuts import render, HttpResponse, redirect
from .models import Restaurant, RestaurantManager, Event
from Location.models import *
from django.contrib import messages

def index(request):

    # Sort by most recent day
    context = {
        'events' : Event.objects.all()
    }
    return render(request,'events.html',context)

#Route is /event/new/create
def createEvent(request):
    #Make sure a restaurant is logged in
    #if "restaurantID" in request.session:
        errors = Event.objects.validator(request.POST)
        print(f"Date: {request.POST['date']}")
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect("/event/new")
        else:
            #Get restaurant object that is currently logged in
            restaurant = Restaurant.objects.get(id=request.session['restaurantID'])
            #Create the location for the event
            location = Location.objects.create(
                address = request.POST["address"],
                city = request.POST["city"],
                state = request.POST["state"],
                zip_code = request.POST["zip_code"]
            )
            #Create the event
            Event.objects.create(
                restaurant_id = restaurant,
                menu = restaurant.menus.first(),
                location= location,
                date_time = request.POST['date'],
                notes = request.POST["notes"],
                minimum_orders = request.POST["min_orders"],
                maximum_orders = 10000, #value is currently a placeholder to say lots of orders
                minimum_amount_per_order = request.POST["min_per_order"]
            )
            return redirect('/event')
    #else:
    #    return redirect('/')

#Route is /event/new
def newEvent(request):
    return render(request, "newEvent.html")