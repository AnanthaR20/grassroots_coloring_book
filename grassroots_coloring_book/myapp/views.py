from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request,"home.html") #HttpResponse("hello world!")

def base(request):
    return render(request,"base.html")

def hello_page(request):
    return HttpResponse("hello world! :o")

def todos(request):
    """Get a list of all instances of the TodoItem"""
    items = TodoItem.objects.all()
    return render(request,"todos.html",{"todos":items})

