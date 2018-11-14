from django.shortcuts import render
from user.models import User
from django.forms import model_to_dict
from django.db.models import Avg
from django.db.models import Q
from django.db.models import IntegerField
import numpy
import parsed as ps
import pandas as pd
from sklearn.externals import joblib
import random
from scipy.integrate import quad

# Create your views here.


def normalProbabilityDensity(x):
    constant = 1.0 / numpy.sqrt(2*numpy.pi)
    return(constant * numpy.exp((-x**2) / 2.0) )


def yniScore(request):

    # user 정보
    user = request.session['authuser']
    user_info = {'ass_fin':user['ASS_FIN'], 'm_tot_saving': user['M_TOT_SAVING'], 'tot_sobi': user['TOT_SOBI'] }

    #금융자산 , 월 저축금액, 월 소비 금액
    result =User.objects.filter(SEX_GBN= user['SEX_GBN'], AGE_GBN= user['AGE_GBN'],INCOME_GBN =user['INCOME_GBN'])\
        .aggregate(Avg('ASS_FIN'),Avg('M_TOT_SAVING'),Avg('TOT_SOBI'))




    # 점수
    score_set=User.objects.filter(SEX_GBN= user['SEX_GBN'], AGE_GBN= user['AGE_GBN'], INCOME_GBN =user['INCOME_GBN'])\
        .values('ASS_FIN', 'M_TOT_SAVING','TOT_SOBI')



    ASS_FIN_list =[]
    M_TOT_SAVING_list =[]
    TOT_SOBI_list =[]


    for score in score_set:
        for key, value in score.items():
            if key == 'ASS_FIN':
                ASS_FIN_list.append(value)
            elif key == 'M_TOT_SAVING':
                M_TOT_SAVING_list.append(value)
            elif key == 'TOT_SOBI':
                TOT_SOBI_list.append(value)



    #금융자산 점수
    ASS_FIN_std = float(numpy.std(ASS_FIN_list))

    user['ASS_FIN'] = float(user['ASS_FIN'])
    result['ASS_FIN__avg'] = float(result['ASS_FIN__avg'])
    ASS_FIN_zscore =  (user['ASS_FIN']-result['ASS_FIN__avg'])/ASS_FIN_std

    ASS_FIN_score, _ = quad(normalProbabilityDensity, numpy.NINF, ASS_FIN_zscore)
    ASS_FIN_score =round(ASS_FIN_score*100)



    #월 저축예금 M_TOT_SAVING
    M_TOT_SAVING_std = float(numpy.std(M_TOT_SAVING_list))

    user['M_TOT_SAVING'] = float(user['M_TOT_SAVING'])
    result['M_TOT_SAVING__avg'] = float(result['M_TOT_SAVING__avg'])
    M_TOT_SAVING_zscore = (user['M_TOT_SAVING'] - result['M_TOT_SAVING__avg']) / M_TOT_SAVING_std

    M_TOT_SAVING_score, _ = quad(normalProbabilityDensity, numpy.NINF, M_TOT_SAVING_zscore)
    M_TOT_SAVING_score = round(M_TOT_SAVING_score * 100)

    # 월 소비금액 TOT_SOBI
    TOT_SOBI_std = float(numpy.std(TOT_SOBI_list))

    user['TOT_SOBI'] = float(user['TOT_SOBI'])
    result['TOT_SOBI__avg'] = float(result['TOT_SOBI__avg'])
    TOT_SOBI_zscore = (user['TOT_SOBI'] - result['TOT_SOBI__avg']) / TOT_SOBI_std

    TOT_SOBI_score, _ = quad(normalProbabilityDensity, numpy.NINF, TOT_SOBI_zscore)
    TOT_SOBI_score = round(TOT_SOBI_score * 100)


    score ={'ASS_FIN_score':ASS_FIN_score,'M_TOT_SAVING_score':M_TOT_SAVING_score,'TOT_SOBI_score':(100-TOT_SOBI_score)}

    print(score)
    result['ASS_FIN__avg'] = round(result['ASS_FIN__avg'])
    result['M_TOT_SAVING__avg'] = round(result['M_TOT_SAVING__avg'])
    result['TOT_SOBI__avg'] = round(result['TOT_SOBI__avg'])

    content = {'detail_avg': result, 'user_info':user_info,'score':score}


    return render(request, 'service/yniScore.html',content)


def yniCompare(request):
    user=request.session['authuser']


    cmp_list = User.objects.filter(SEX_GBN=user['SEX_GBN'], AGE_GBN=user['AGE_GBN'], INCOME_GBN=user['INCOME_GBN'])\
        .aggregate(Avg('M_TOT_SAVING',output_field=IntegerField()), Avg('M_JEOK',output_field=IntegerField()), Avg('CHUNG_Y',output_field=IntegerField()),
                   Avg('CHUNG_Y',output_field=IntegerField()), Avg('M_FUND_STOCK',output_field=IntegerField()), Avg('M_FUND',output_field=IntegerField()),
                   Avg('M_STOCK',output_field=IntegerField()), Avg('M_SAVING_INSUR',output_field=IntegerField()), Avg('M_CHUNG',output_field=IntegerField()),
                   Avg('TOT_DEBT',output_field=IntegerField()), Avg('D_SHINYONG',output_field=IntegerField()), Avg('D_DAMBO',output_field=IntegerField()),
                   Avg('D_JUTEAKDAMBO',output_field=IntegerField()), Avg('D_JEONSEA',output_field=IntegerField()), Avg('RETIRE_NEED',output_field=IntegerField()),
                   Avg('FOR_RETIRE',output_field=IntegerField()), Avg('TOT_YEA',output_field=IntegerField()), Avg('TOT_ELS_ETE',output_field=IntegerField()),
                   Avg('TOT_JEOK',output_field=IntegerField()),
                   Avg('TOT_CHUNG',output_field=IntegerField()), Avg('TOT_FUND',output_field=IntegerField()), Avg('CHUNG_Y',output_field=IntegerField()),
                   Avg('TOT_SOBI',output_field=IntegerField()), Avg('M_CRD_SPD',output_field=IntegerField())
                         )


    for key in cmp_list.keys():
        if  cmp_list[key] == 0:
            cmp_list[key] = '없음'
        else :
            cmp_list[key] = str(cmp_list[key])+' 만원'

    del user['name']
    del user['email']
    del user['password']
    del user['idx']
    del user['SEX_GBN']
    del user['AGE_GBN']
    del user['JOB_GBN']
    del user['ADD_GBN']
    del user['INCOME_GBN']
    del user['MARRY_Y']
    del user['DOUBLE_IN']
    del user['NUMCHILD']
    del user['TOT_ASSET']
    del user['ASS_FIN']
    del user['ASS_REAL']
    del user['ASS_ETC']
    print(user)

    for key in user.keys():
        if user[key] == 0:
            user[key] = '없음'
        else:
            user[key] = str(user[key])+' 만원'


    content ={'user':user, 'cmp':cmp_list}
    print(content)

    return render(request, 'service/yniCompare.html',content)


def yniAverage(request):
    #내정보로 부터 검색
    idx = request.session['authuser']['idx']
    #기본정보
    sex_list =['','남자','여자']
    age_list =['','20대','30대','40대','50대','60세이상']
    add_list =['','강남3구_송파,강남,서초','서울 기타','광역시','경기도','기타']
    job_list =['','기타','사무직','공무원','전문직(근로직)','전문직(자영업)','판매서비스',
               '기능직','일반 자영업','프리랜서','학생']
    income_list = ['미응답','100만원 미만','200만원 미만','300만원 미만','400만원 미만','500만원 미만'
                   ,'600만원 미만','700만원 이상']


    #상세정보
    marry_list = ['미응답','미혼','기혼']  #결혼여부
    double_list = ['미응답','외벌이','맞벌이'] #맞벌이
    numchild_list= ['미응답','1명','2명','3명이상'] #자녀수
    user = User.objects.filter(idx =idx)[0]
    sex_gbn =  user.SEX_GBN
    age_gbn = user.AGE_GBN
    income_gbn = user.INCOME_GBN
    job_gbn=user.JOB_GBN
    add_gbn = user.ADD_GBN

    numchild = user.NUMCHILD
    #상세정보
    marry_y = user.MARRY_Y  #결혼유무
    double_y = user.DOUBLE_IN #맞벌이 유무
    ass_fin = user.ASS_FIN
    m_tot_saving = user.M_TOT_SAVING
    tot_sobi = user.TOT_SOBI


    print(sex_list[sex_gbn])
    print(age_list[age_gbn])
    print(ass_fin)
    print(m_tot_saving)
    print(tot_sobi)
    user_info ={'sex':sex_list[sex_gbn], 'age':age_list[age_gbn], 'income':income_list[income_gbn],
                'job':job_list[job_gbn],'add':add_list[add_gbn],
                'marry':marry_list[marry_y], 'double':double_list[double_y], 'numchild':numchild_list[numchild],
                'ass_fin':ass_fin, 'm_tot_saving':m_tot_saving, 'tot_sobi':tot_sobi}







    #전체비중
    total_cnt =User.objects.filter(SEX_GBN= sex_gbn, AGE_GBN= age_gbn,INCOME_GBN =income_gbn).count()
    #나와 같은 직업 비중
    job_gbn_cnt = User.objects.filter(SEX_GBN=sex_gbn, AGE_GBN=age_gbn, INCOME_GBN=income_gbn).filter(JOB_GBN=job_gbn) \
    .count()
    #나와 같은 지역 비중
    add_gbn_cnt = User.objects.filter(SEX_GBN=sex_gbn, AGE_GBN=age_gbn, INCOME_GBN=income_gbn).filter(ADD_GBN=add_gbn) \
    .count()
    #결혼 여부
    marry_y_cnt= User.objects.filter(SEX_GBN=sex_gbn, AGE_GBN=age_gbn, INCOME_GBN=income_gbn).filter(MARRY_Y='2') \
    .count()
    marry_n_cnt= User.objects.filter(SEX_GBN=sex_gbn, AGE_GBN=age_gbn, INCOME_GBN=income_gbn).filter(MARRY_Y='0') \
    .count()
    marry_t_cnt = total_cnt -marry_n_cnt
    #맞벌이 유무 비율
    double_cnt=User.objects.filter(SEX_GBN= sex_gbn, AGE_GBN= age_gbn,INCOME_GBN =income_gbn).filter(DOUBLE_IN='2')\
    .count()

    double_t_cnt=User.objects.filter(SEX_GBN= sex_gbn, AGE_GBN= age_gbn,INCOME_GBN =income_gbn).filter(~Q(DOUBLE_IN='0'))\
    .count()



    #자녀수
    numchild_cnt = User.objects.filter(SEX_GBN= sex_gbn, AGE_GBN= age_gbn,INCOME_GBN =income_gbn).filter(~Q(NUMCHILD ='0'))\
    .aggregate(Avg('NUMCHILD'))
    numchild_cnt = round(numchild_cnt['NUMCHILD__avg'])
   # numchild_cnt = round(numchild_cnt)
   # print("numchild: %s" %numchild_cnt)
    #월소득 평균
    total_avg =User.objects.filter(SEX_GBN= sex_gbn, AGE_GBN= age_gbn,INCOME_GBN =income_gbn)\
    .aggregate(Avg('M_TOT_SAVING'),Avg('TOT_SOBI'))
    total_result = round(total_avg['M_TOT_SAVING__avg']+total_avg['TOT_SOBI__avg'])


    #모두계산
    job_gbn_result = round((job_gbn_cnt/total_cnt)*100)
    add_gbn_result = round((add_gbn_cnt/total_cnt) *100)
    marry_y_result = round((marry_y_cnt/marry_t_cnt) *100)
    double_result = round((double_cnt/double_t_cnt) *100)

    #금융자산 , 월 저축금액, 월 소비 금액
    result =User.objects.filter(SEX_GBN= sex_gbn, AGE_GBN= age_gbn,INCOME_GBN =income_gbn)\
        .aggregate(Avg('ASS_FIN'),Avg('M_TOT_SAVING'),Avg('TOT_SOBI'))



    result['ASS_FIN__avg']  =  round(result['ASS_FIN__avg'])
    result['M_TOT_SAVING__avg']  =  round(result['M_TOT_SAVING__avg'])
    result['TOT_SOBI__avg']  =  round(result['TOT_SOBI__avg'])




    content = {'detail_avg': result, 'double_result':double_result, 'job_gbn_result':job_gbn_result,
               'add_gbn_result':add_gbn_result,'marry_y_result':marry_y_result,
               'numchild_result':numchild_cnt,'total_result':total_result,'user_info':user_info
               }



    return render(request, 'service/yniAverage.html', content)


def productList(request):
    dic={}
    # pnum = request.session['authuser']['Product']
    # print("pnum %s" %pnum)
    # pnum = 4

    # Load from file
    joblib_model = joblib.load("joblib_model.pkl")


    user = request.session['authuser']
    train = {'AGE_GBN': [user['AGE_GBN']],
             "MARRY_Y": [user['MARRY_Y']],
             "JOB_GBN": [user['JOB_GBN']],
             "ADD_GBN": [user['ADD_GBN']],
             "INCOME_GBN": [user['INCOME_GBN']],
             "NUMCHILD": [user['NUMCHILD']],
             'TOT_ASSET': [user['TOT_ASSET']],
             'CHUNG_Y': [user['CHUNG_Y']],
             'TOT_DEBT': [user['TOT_DEBT']],
             'D_JUTEAKDAMBO': user['D_JUTEAKDAMBO'],
             'RETIRE_NEED': user['RETIRE_NEED'],
             'FOR_RETIRE': [user['FOR_RETIRE']],
             'TOT_SOBI': [user['TOT_SOBI']]}

    print(train)
    train = pd.DataFrame(train)

    Y_predict = joblib_model.predict(train)
    print(Y_predict)
    pnum = Y_predict
    print(pnum)
    dic['num1'] = random.randrange(101, 150)
    dic['num2'] = random.randrange(51, 100)
    dic['num3'] = random.randrange(31, 50)
    dic['num4'] = random.randrange(10, 30)

    pnum=5
    if pnum == 2 or pnum == 1 or pnum == 7:
        dic['result'] = ps.yeaDriver()

        content = dic
        return render(request, 'service/recommendList_yea.html', content)
    elif pnum == 3:
        dic['result']= ps.jeok()
        content = dic
        return render(request, 'service/recommendList_jeok.html', content)
    elif pnum == 4:
        dic['result'] = ps.renteDriver()
        content = dic
        return render(request, 'service/recommendList_renteDriver.html', content)

    elif pnum == 5:
        dic['result'] = ps.juteakDambo()
        content = dic
        return render(request, 'service/recommendList_juteakDambo.html', content)

    elif pnum == 6:
        dic['result'] = ps.shinyong()
        content = dic
        return render(request, 'service/recommendList_shinyong.html', content)

    elif pnum == 7:

        print("juteakChung")

