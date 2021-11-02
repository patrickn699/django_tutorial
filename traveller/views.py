from django.shortcuts import render
from django.http import HttpResponse
from .models import desti

# Create your views here.
def welcome(request):
    dest = desti()
    dest.price = 100
    dest.img = 'destination_1.jpg'
    dest.name = 'Mumbai'
    dest.desc = 'The city that never sleeps'
    dest.offer = False

    dest1 = desti()
    dest1.price = 200
    dest1.img = 'destination_2.jpg'
    dest1.name = 'Delhi'
    dest1.desc = 'The city that never sleeps'
    dest1.offer = True

    dest2 = desti()
    dest2.price = 300
    dest2.img = 'destination_3.jpg'
    dest2.name = 'Kolkata'
    dest2.desc = 'The city that never sleeps'
    dest2.offer = False

    dests = [dest,dest1,dest2]

    return render(request, 'index2.html',{'dests':dests})