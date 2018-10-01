from django.forms import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User


def joinform(request):
    return render(request,'user/joinform.html')

# 사용자가 입력한 값을 넣어줌

def join(request):
    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    user.save()
    # redirect로 joinsuccess로 돌아간다.
    return HttpResponseRedirect('/user/joinsuccess')

def joinsuccess(request):
    return render(request,'user/joinsuccess.html')

def loginform(request):
    return render(request,'user/loginform.html')


def login(request):

    # 쿼리를 부른다.
    result = User.objects.filter(email = request.POST['email']).filter(password = request.POST['password'])

    # 로그인 실패
    if len(result) == 0:
        return HttpResponseRedirect('/user/loginform?result=False')
    print(result[0])
    # 로그인 성공할 때만 저장(인증처리)
    authuser= result[0]

    request.session['authuser'] = model_to_dict(authuser) # 세션에다 객체를 넣는지 않넣는지로 판단. model_to_dict를 통해 dict값으로 넘긴다.
    #return HttpResponse('hello user') # 브라우저에 헬로 월드가 나온거는 인증이 됬다는 것이다.
    return HttpResponseRedirect('/') # 메인으로 돌아간다.

def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/') # 다시 메인 홈페이지로 이동