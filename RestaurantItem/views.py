from django.shortcuts import render, HttpResponse, redirect
from .models import Item

def index(request):
    
    # Sort by most recent day
    context = {
        'items' : Item.objects.all()
    }
    return render(request,'items.html',context)