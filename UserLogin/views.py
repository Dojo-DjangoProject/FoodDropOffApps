from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Works')

def users(request):
    return render(request,'user_login.html')
    
def user_info(request,user_id):
    return render(request,'user_welcome.html')