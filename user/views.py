from django.forms import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User


def joinform(request):
    return render(request, 'user/joinform.html')


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
    return render(request, 'user/joinsuccess.html')


def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    # 쿼리를 부른다.
    result = User.objects.filter(email=request.POST['email']).filter(password=request.POST['password'])

    # 로그인 실패
    if len(result) == 0:
        return HttpResponseRedirect('/user/loginform?result=False')
    print(result[0])
    # 로그인 성공할 때만 저장(인증처리)
    authuser = result[0]

    request.session['authuser'] = model_to_dict(authuser)  # 세션에다 객체를 넣는지 않넣는지로 판단. model_to_dict를 통해 dict값으로 넘긴다.
    # return HttpResponse('hello user') # 브라우저에 헬로 월드가 나온거는 인증이 됬다는 것이다.
    return HttpResponseRedirect('/')  # 메인으로 돌아간다.


def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')  # 다시 메인 홈페이지로 이동


def mypage(request):
    # guestbook_list = Guestbook1.objects.all().order_by('-regdate')
    # context = {'guestbook_list': guestbook_list}

    return render(request, 'user/mypage.html')  # mypage.html 로 이동


def mypage_submit(request):
    user = User()

    user.name = request.POST['name']

    user.SEX_GBN = request.POST.get['SEX_GBN']
    user.AGE_GBN = request.POST.get['AGE_GBN']
    user.JOB_GBN = request.POST.get['JOB_GBN']
    user.ADD_GBN = request.POST.get['ADD_GBN']
    user.INCOME_GBN = request.POST.get['INCOME_GBN']
    user.MARRY_Y = mrequest.POST.get['MARRY_Y']
    user.DOUBLE_IN = request.POST.get['DOUBLE_IN']
    user.NUMCHILD = request.POST.get['NUMCHILD']
    user.TOT_ASSET = request.POST.get['TOT_ASSET']
    user.ASS_FIN = request.POST.get['ASS_FIN']
    user.ASS_REAL = request.POST.get['ASS_REAL']
    user.ASS_ETC = request.POST.get['ASS_ETC']
    user.M_TOT_SAVING = request.POST.get['M_TOT_SAVING']
    user.M_JEOK = request.POST.get['M_JEOK']
    user.CHUNG_Y = request.POST.get['CHUNG_Y']
    user.M_FUND_STOCK = request.POST.get['M_FUND_STOCK']
    user.M_FUND = request.POST.get['M_FUND']
    user.M_STOCK = request.POST.get['M_STOCK']
    user.M_SAVING_INSUR = request.POST.get['M_SAVING_INSUR']
    user.M_CHUNG = request.POST.get['M_CHUNG']
    user.TOT_DEBT = request.POST.get['TOT_DEBT']
    user.D_SHINYONG = request.POST.get['D_SHINYONG']
    user.D_DAMBO = request.POST.get['D_DAMBO']
    user.D_JUTEAKDAMBO = request.POST.get['D_JUTEAKDAMBO']
    user.D_JEONSEA = request.POST.get['D_JEONSEA']
    user.RETIRE_NEED = request.POST.get['RETIRE_NEED']
    user.FOR_RETIRE = request.POST.get['FOR_RETIRE']
    user.TOT_YEA = request.POST.get['TOT_YEA']
    user.TOT_JEOK = request.POST.get['TOT_JEOK']
    user.TOT_CHUNG = request.POST.get['TOT_CHUNG']
    user.TOT_FUND = request.POST.get['TOT_FUND']
    user.TOT_ELS_ETE = request.POST.get['TOT_ELS_ETE']
    user.TOT_SOBI = request.POST.get['TOT_SOBI']
    user.M_CRD_SPD = request.POST.get['M_CRD_SPD']

    user.save()
    return HttpResponseRedirect('user/mypage.html')
