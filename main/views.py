from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    try:
        if request.session['authuser'] is not None:

            return HttpResponseRedirect('/user/mypage')
    except:
        return render(request, 'main/main.html')