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
    # 로그인된 객체를 가져온다.
    #idx = request.session['authuser']['idx']
    # result =User.objects.filter(idx= idx)
    #
    # user = result[0]
    # authuser=model_to_dict(user)
    # print(authuser)
    content ={'user' : request.session['authuser']}
    print(content)
    return render(request, 'user/mypage.html',content)  # mypage.html 로 이동


def mypage_submit(request):

    #로그인 유저의 idx에 해당하는 객체얻어옴
    idx = request.session['authuser']['idx']
    result =User.objects.filter(idx= idx)

    user = result[0]

    print(user)
    user.name = request.POST.get('name', '')

    print(user.name)

    user.SEX_GBN = request.POST.get('SEX_GBN', '0')
    user.AGE_GBN = request.POST.get('AGE_GBN', '0')

    user.JOB_GBN = request.POST.get('JOB_GBN', '0')
    user.ADD_GBN = request.POST.get('ADD_GBN', '0')
    user.INCOME_GBN = request.POST.get('INCOME_GBN', '0')
    user.MARRY_Y = request.POST.get('MARRY_Y', '0')
    user.DOUBLE_IN = request.POST.get('DOUBLE_IN', '0')
    user.NUMCHILD = request.POST.get('NUMCHILD', '0')
    user.TOT_ASSET  =request.POST.get('TOT_ASSET','0')
    user.ASS_FIN = request.POST.get('ASS_FIN', '0')
    user.ASS_REAL = request.POST.get('ASS_REAL', '0')
    user.ASS_ETC = request.POST.get('ASS_ETC', '0')
    user.M_TOT_SAVING = request.POST.get('M_TOT_SAVING', '0')
    user.M_JEOK = request.POST.get('M_JEOK', '0')
    user.CHUNG_Y = request.POST.get('CHUNG_Y', '0')
    user.M_FUND_STOCK = request.POST.get('M_FUND_STOCK', '0')
    user.M_FUND = request.POST.get('M_FUND', '0')
    user.M_STOCK = request.POST.get('M_STOCK', '0')
    user.M_SAVING_INSUR = request.POST.get('M_SAVING_INSUR', '0')
    user.M_CHUNG = request.POST.get('M_CHUNG', '0')
    user.TOT_DEBT = request.POST.get('TOT_DEBT', '0')
    user.D_SHINYONG = request.POST.get('D_SHINYONG', '0')
    user.D_DAMBO = request.POST.get('D_DAMBO', '0')
    user.D_JUTEAKDAMBO = request.POST.get('D_JUTEAKDAMBO', '0')
    user.D_JEONSEA = request.POST.get('D_JEONSEA', '0')
    user.RETIRE_NEED = request.POST.get('RETIRE_NEED', '0')
    user.FOR_RETIRE = request.POST.get('FOR_RETIRE', '0')
    user.TOT_YEA = request.POST.get('TOT_YEA', '0')
    user.TOT_JEOK = request.POST.get('TOT_JEOK', '0')
    user.TOT_CHUNG = request.POST.get('TOT_CHUNG', '0')
    user.TOT_FUND = request.POST.get('TOT_FUND', '0')
    user.TOT_ELS_ETE = request.POST.get('TOT_ELS_ETE', '0')
    user.TOT_SOBI = request.POST.get('TOT_SOBI', '0')
    user.M_CRD_SPD = request.POST.get('M_CRD_SPD', '0')
    user.Check_field = 1
    # 유저세션 업데이트
    user.save()
    request.session['authuser'] = model_to_dict(user)

    return HttpResponseRedirect('/user/mypage')