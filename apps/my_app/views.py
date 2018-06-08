from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Dojo, Ninjas

def index(request):
    return render(request, 'my_app/index.html')



