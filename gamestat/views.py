from django.shortcuts import render
from models import Platform, Statistic, Genre
from django.contrib.auth.models import User


def home(request):
    
    return render (request, "page/homepage.html")



# Create your views here.
