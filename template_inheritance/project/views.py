from django.shortcuts import HttpResponse,render
from datetime import datetime,timedelta

def home(request):
    return render(request,"home.html") 

def contact(request):
    return render(request,"contact.html") 

def about(request):
    return render(request,"about.html")