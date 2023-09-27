from django.shortcuts import render
from django.http import HttpResponse
from .models import Shop
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import os
import shutil
from datetime import datetime
from django.utils import timezone

# Create your views here.

@csrf_exempt
def update(request):
    inst = Shop.objects.all()[0]

    
