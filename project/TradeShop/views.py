from django.shortcuts import render
from django.http import HttpResponse
from .models import Exchange
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import os
import shutil
import random

from account.models import User, Ingame

# Create your views here.


@csrf_exempt
def update(request):
    allinst = Exchange.objects.all()
    bupper = []

    for a in allinst:
        tempname = a.name

        query = Ingame.objects.filter(name=tempname)

        if query:
            continue
        else:
            bupper.append(str(a))

    random.shuffle(bupper)
    if (len(bupper) > 12):
        rtvalue = '?'.join(bupper[:12])
    else:
        rtvalue = '?'.join(bupper)
    return HttpResponse(rtvalue)


@csrf_exempt
def upload(request):
    _item_code = request.GET['item_code']
    _price = request.GET['price']
    _name = request.GET['name']

    newExc = Exchange(item_code=_item_code, price=_price, name=_name)
    try:
        newExc.save(force_insert=True)
        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse('0')


@csrf_exempt
def buy(request):
    _item_code = request.GET['item_code']
    _price = request.GET['price']
    _name = request.GET['name']

    # give money
    tempname = User.objects.get(name=_name)
    tempname.coin += int(_price)
    tempname.save()
    
    try:
        inst = Exchange.objects.get(item_code=_item_code, price=_price, name=_name)
        inst.delete()
        return HttpResponse('1')

    except Exception as e:
        print(e)
        return HttpResponse('0')


@csrf_exempt
def delete(request):
    allinst = Exchange.objects.all()

    for a in allinst:
        a.delete()

    return HttpResponse('done')

