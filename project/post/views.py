from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload(request):
    _name = request.GET['name']
    _text = request.GET['text']

    allinst = list(Post.objects.all())
    allinst.sort(key=lambda x : x.regtime)

    if len(allinst) > 6:
        topbp = Chat.objects.get(regtime=allinst[0].regtime)
        topbp.delete()

    inst = Post(name=_name, text=_text)
    try:
        inst.save(force_insert=True)
        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse('1')


@csrf_exempt
def update(request):
    allinst = list(Post.objects.all())
    allinst.sort(key=lambda x : x.regtime)

    rtlist = list(map(lambda x : str(x), allinst))
    rtvalue = '$'.join(rtlist)

    return HttpResponse(rtvalue)

@csrf_exempt
def delete(request):
    allinst = Post.objects.all()

    for a in allinst:
        a.delete()

    return HttpResponse('done')
