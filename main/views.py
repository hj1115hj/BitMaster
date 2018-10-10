from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        if request.session['authuser'] is not None:
            return render(request, 'user/mypage.html')
    except:
        return render(request, 'main/main.html')