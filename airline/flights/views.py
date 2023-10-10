from django.shortcuts import render
from .models import FLIGHT
# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        "flights":FLIGHT.objects.all()
    })