from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")
def index1(request):
    return render(request, "login/FIRST_webpage.html")
def index2(request):
    return render(request, "Boot_app/home.html")
def index3(request):
    return render(request, "Boot_app/Assignment_page2.html")
def index4(request):
    return render(request, "Boot_app/aassignment3.html")
