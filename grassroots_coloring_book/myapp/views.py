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
    print(items)
    return render(request,"todos.html",{"todos":items})

def display_prompt(request):
    a = input("type the first header\n")
    b = input("type the second header\n")
    c = [i for i in range(10)]
    print({"key":a})
    return render(request,"home2.html",{"h1":a,"h2":b,"h3":c})