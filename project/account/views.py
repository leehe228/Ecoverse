from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Ingame
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import os
import shutil


@csrf_exempt
def save(request):
    _name = request.GET['name']
    _player = request.GET['player']

    _mission_state = request.GET['mission_state']
    _submission_state = request.GET['submission_state']
    _museum_unlock = request.GET['museum_unlock']

    _soil_item_unlock = request.GET['soil_item_unlock']
    _energy_item_unlock = request.GET['energy_item_unlock']

    _coin = request.GET['coin']
    _furniture_state = request.GET['furniture_state']
    _smartfarm_state = request.GET['smartfarm_state']

    _inventory_state = request.GET['inventory_state']

    _ecomileage = request.GET['ecomileage']

    _badge_state = request.GET['badge_state']
    _badge_subinfo = request.GET['badge_subinfo']

    _character_unlock = request.GET['character_unlock']
    
    try:
        i = User.objects.get(name=_name)
        i.player = int(_player)
        i.mission_state = int(_mission_state)
        i.submission_state = _submission_state
        i.museum_unlock = int(_museum_unlock)
        i.soil_item_unlock = int(_soil_item_unlock)
        i.energy_item_unlock = int(_energy_item_unlock)
        i.coin = int(_coin)
        i.furniture_state = _furniture_state
        i.smartfarm_state = _smartfarm_state
        i.inventory_state = _inventory_state
        i.ecomileage = int(_ecomileage)
        i.badge_state = _badge_state
        i.badge_subinfo = _badge_subinfo
        i.character_unlock = _character_unlock
        
        i.save()
        return HttpResponse('1')

    except Exception as e:
        print(e)
        return HttpResponse('0')


@csrf_exempt
def load(request):
    _name = request.GET['name']

    bp = User.objects.get(name=_name)

    return HttpResponse(str(bp))


@csrf_exempt
def hello(request):
    return HttpResponse('HELLO')


@csrf_exempt
def login(request):
    _email = request.GET['email']
    _password = request.GET['password']

    queryset = User.objects.filter(email=_email, password=_password)
    
    if queryset:
        inst = User.objects.get(email=_email)
        return HttpResponse(inst.name)
    else:
        # not registered
        return HttpResponse('0')


@csrf_exempt
def register(request):
    _email = request.GET['email']
    _password = request.GET['password']
    _name = request.GET['name']

    queryset = User.objects.filter(email=_email, password=_password)
    
    # already registered
    if queryset:
        return HttpResponse('-1')

    queryset = User.objects.filter(name=_name)

    if queryset:
        return HttpResponse('-2')

    newUser = User(email=_email, password=_password, name=_name)

    try:
        newUser.save(force_insert=True)
        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse('0')


@csrf_exempt
def gamein(request):
    _name = request.GET['name']
    _player = request.GET['player']

    queryset = Ingame.objects.filter(name=_name)

    if queryset:
        return HttpResponse('-1')

    newInstance = Ingame(name=_name, player=int(_player))

    try:
        newInstance.save(force_insert=True)
        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse('0')


@csrf_exempt
def update(request):
    _name = request.GET['name']
    _px = request.GET['px']
    _py = request.GET['py']
    _pz = request.GET['pz']
    _rx = request.GET['rx']
    _ry = request.GET['ry']
    _rz = request.GET['rz']

    try:
        instance = Ingame.objects.get(name=_name)
        instance.posx = _px
        instance.posy = _py
        instance.posz = _pz
        instance.rotx = _rx
        instance.roty = _ry
        instance.rotz = _rz
        instance.save()
        
        allinst = Ingame.objects.all()
        rtlist = list(map(lambda x : str(x), allinst))
        rtvalue = '?'.join(rtlist)

        return HttpResponse(rtvalue)

    except Exception as e:
        print(e)
        return HttpResponse('-1')

@csrf_exempt
def gameout(request):
    _name = request.GET['name']

    queryset = Ingame.objects.filter(name=_name)

    if queryset:
        try:
            instance = Ingame.objects.get(name=_name)
            instance.delete()
            return HttpResponse('1')
        except Exception as e:
            print(e)
            return HttpResponse('0')

    else:
        return HttpResponse('-1')


@csrf_exempt
def delete(request):
    allinst = User.objects.all()

    for a in allinst:
        a.delete()

    return HttpResponse('done')


#
