from email import message
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def index(request):
    context = {
        "ingredients": Ingredient.objects.all(),
        "menu_items": MenuItem.objects.all(),
        "purchases": Purchase.objects.all(), 
    }
    return render(request, "inventory/index.html", context)

def ingredients(request):
    
