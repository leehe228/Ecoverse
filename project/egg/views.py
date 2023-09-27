from django.shortcuts import render
from django.http import HttpResponse
from .models import Egg
from django.views.decorators.csrf import csrf_exempt

import random

# Create your views here.

@csrf_exempt
def getrpos():
    x = 0
    z = 0

    while True:
        x = random.randrange(-160, 160)
        z = random.randrange(-160, 160)
        
        # outer circle
        if 160**2 < (x - 0)**2 + (z - 30)**2:
            continue
        
        # car road
        if 155**2 > (x - 0)**2 + (z - 30)**2 > 131**2:
            continue
        
        # soccer
        if -10 < x < 96 and 43 < z < 131:
            continue

        # buildings
        if -113 < x < -29 and 17 < z < 108:
            continue

        # left shop
        if -109 < x < -63 and -52 < z < -6:
            continue

        # right shop
        if 63 < x < 109 and -52 < z < -6:
            continue

        # museums
        if -69 < x < 69 and 8 < z < 37:
            continue

        # inner
        if -18 < x < 18:
            continue

        break

    return x, z

@csrf_exempt
def update(request):
    allinst = Egg.objects.all()

    rtlist = list(map(lambda x : str(x), allinst))
    rtvalue = '?'.join(rtlist)

    return HttpResponse(rtvalue)


@csrf_exempt
def suf(request):
    allinst = Egg.objects.all()
    
    for i in allinst:
        _x, _z = getrpos()
        i.pos = str(_x) + '/' + str(_z)
        i.save()

    return HttpResponse('done')


@csrf_exempt
def eat(request):
    _num = request.GET['num']

    instance = Egg.objects.get(number=_num)

    x, z = getrpos()

    instance.pos = str(x) + '/' + str(z)
    instance.save()

    return HttpResponse('0')



