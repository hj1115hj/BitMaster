# Create your models here.
from django.db import models


class User(models.Model):

    name = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    idx = models.AutoField(primary_key=True)
    SEX_GBN = models.IntegerField(default=0)  # 성별
    AGE_GBN = models.IntegerField(default=0)  # 연령-10세단위
    JOB_GBN = models.IntegerField(default=0)  # 직업
    ADD_GBN = models.IntegerField(default=0)  # 지역
    INCOME_GBN = models.IntegerField(default=0)  # 가구소득구간
    MARRY_Y = models.IntegerField(default=0)  # 결혼여부
    DOUBLE_IN = models.IntegerField(default=0)  # 맞벌이
    NUMCHILD = models.IntegerField(default=0)  # 자녀수
    TOT_ASSET = models.IntegerField(default=0)  # 총자산
    ASS_FIN = models.IntegerField(default=0)  # 금융자산
    ASS_REAL = models.IntegerField(default=0)  # 부동산자산
    ASS_ETC = models.IntegerField(default=0)  # 기타자산
    M_TOT_SAVING = models.IntegerField(default=0)  # 월총저축액
    M_JEOK = models.IntegerField(default=0)  # 월저축액_적금
    CHUNG_Y = models.IntegerField(default=0)  # 청약보유여부
    M_FUND_STOCK = models.IntegerField(default=0)  # 월저축액_펀드/주식
    M_FUND = models.IntegerField(default=0)  # 월저축액_펀드
    M_STOCK = models.IntegerField(default=0)  # 월저축액_주식
    M_SAVING_INSUR = models.IntegerField(default=0)  # 월저축액_저축성보험
    M_CHUNG = models.IntegerField(default=0)  # 월저축액_청약
    TOT_DEBT = models.IntegerField(default=0)  # 부채잔액
    D_SHINYONG = models.IntegerField(default=0)  # 부채잔액_신용대출
    D_DAMBO = models.IntegerField(default=0)  # 부채잔액_담보대출
    D_JUTEAKDAMBO = models.IntegerField(default=0)  # 부채잔액_아파트/주택담보대출
    D_JEONSEA = models.IntegerField(default=0)  # 부채잔액_전세자금대출
    RETIRE_NEED = models.IntegerField(default=0)  # 은퇴후필요자금
    FOR_RETIRE = models.IntegerField(default=0)  # 노후자금융_월저축액
    TOT_YEA = models.IntegerField(default=0)  # 금융삼품잔액_정기예금
    TOT_JEOK = models.IntegerField(default=0)  # 금융삼품잔액_적금
    TOT_CHUNG = models.IntegerField(default=0)  # 금융삼품잔액_청약
    TOT_FUND = models.IntegerField(default=0)  # 금융삼품잔액_펀드
    TOT_ELS_ETE = models.IntegerField(default=0)  # 금융삼품잔액_ELS/DLS/ETF
    TOT_SOBI = models.IntegerField(default=0)  # 월총소비금액
    M_CRD_SPD = models.IntegerField(default=0)  # 월평균카드사용금액
    Check_field = models.IntegerField(default=0) #값이 모두 입력되어있는지 아닌지 판단

    def __str__(self):
        return 'user(%s, %s %s)' % \
               (self.name, self.email,self.idx)






