from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitMaster.settings")
import django
django.setup()
import time

def juteakDambo():
    print('jeok')
    req = requests.get('http://finlife.fss.or.kr/mortagageloan/selectMortagageLoan.do?menuId=2000102')
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    table_rows = []
    for row in soup.select('#ajaxResult > div.table_area > table > tbody > tr'):
        table_rows.append([td.text.strip() for td in row.find_all('td')])

    print(table_rows)

    data_list = []
    for rows in table_rows:
        r_list = [x for x in rows if x]
        if r_list:
            print(r_list)
            r_dict = {}
            r_dict['co_nm'] = r_list[1]
            r_dict['product_nm'] = r_list[2]
            r_dict['day'] = r_list[3]
            r_dict['money'] = r_list[4]
            r_dict['type'] = r_list[5]
            r_dict['suic'] = r_list[6]
            r_dict['rate'] = r_list[7]
            r_dict['month_yea'] = r_list[8]

            data_list.append(r_dict)

    print(data_list)
    return data_list


def jeok():
    print('jeok')
    req = requests.get('http://finlife.fss.or.kr/installment/selectinstallment.do?menuId=2000101')
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    table_rows = []
    for row in soup.select('#ajaxResult > div.table_area > table > tbody > tr'):
        table_rows.append([td.text.strip() for td in row.find_all('td')])

    print(table_rows)

    data_list=[]
    for rows in table_rows:
        r_list = [x for x in rows if x]
        if r_list:
            print(r_list)
            r_dict = {}
            r_dict['co_nm'] = r_list[1]
            r_dict['product_nm'] = r_list[2]
            r_dict['way'] = r_list[3]
            r_dict['iza1'] = r_list[4]
            r_dict['iza2'] = r_list[5]
            r_dict['iza3'] = r_list[6]
            r_dict['max_rate'] = r_list[7]
            r_dict['join_mem'] = r_list[8]
            r_dict['iza_cal'] = r_list[9]
            data_list.append(r_dict)


    print(data_list)
    return data_list

def yea():
    req = requests.get('http://finlife.fss.or.kr/deposit/selectDeposit.do?menuId=2000100')
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('#ajaxResult > div.table_area > table > tbody > tr')
    data_list=[]
    for idx, post in  enumerate(posts):

        key_list =post.text.split('\n')
        r_list = [x for x in key_list if x]
        if r_list:
            print(r_list)
            r_dict = {}
            r_dict['co_nm'] = r_list[1]
            r_dict['product_nm'] = r_list[2]
            r_dict['iza1'] = r_list[4]
            r_dict['iza2'] = r_list[5]
            r_dict['iza3'] = r_list[6]
            r_dict['max_rate'] = r_list[7]
            r_dict['join_mem'] = r_list[8]
            r_dict['iza_cal'] = r_list[9]
            data_list.append(r_dict)

    print(data_list)
    return data_list

def yeaDriver():
    chrome_path = "C:/Users/user/Downloads/chromedriver/chromedriver.exe"

    driver = webdriver.Chrome(chrome_path)
    # driver = webdriver.Chrome('/Users/user/Downloads/chromedriver_win32')
    ## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
    driver.implicitly_wait(3)

    driver.maximize_window()
    driver.get('http://finlife.fss.or.kr/deposit/selectDeposit.do?menuId=2000100')
    element = driver.find_element_by_id('saving-money01')
    driver.execute_script("arguments[0].setAttribute('value','20000000')", element)

    driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[1]/button').click()

    time.sleep(5)  # 5초 대기

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('#ajaxResult > div.table_area > table > tbody > tr')
    data_list=[]
    for idx, post in  enumerate(posts):

        key_list =post.text.split('\n')
        r_list = [x for x in key_list if x]
        if r_list:
            print(r_list)
            r_dict = {}
            r_dict['co_nm'] = r_list[1]
            r_dict['product_nm'] = r_list[2]
            r_dict['iza1'] = r_list[3]
            r_dict['iza2'] = r_list[4]
            r_dict['iza3'] = r_list[5]
            r_dict['max_rate'] = r_list[6]
            r_dict['join_mem'] = r_list[7]
            r_dict['iza_cal'] = r_list[8]
            data_list.append(r_dict)
    print(data_list)
    driver.quit()  # 브라우저 종료
    return data_list


def shinyong():
    req = requests.get('http://finlife.fss.or.kr/creditfacility/selectCreditfacility.do?menuId=2000104')
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    table_rows = []
    for row in soup.select('#ajaxResult > div.table_area > table > tbody > tr'):
        table_rows.append([td.text.strip() for td in row.find_all('td')])

    print(table_rows)

    data_list=[]
    for idx,rows in enumerate(table_rows):
        if idx % 2 ==0 :
            print("idx ----------")
            print(idx)
            r_list = [x for x in rows if x]
            if r_list:

                r_dict = {}
                print("r_list------------------------------------")
                print(r_list)
                r_dict['co_nm'] = r_list[0]
                r_dict['type'] = r_list[1]
                r_dict['money'] = r_list[2]
                r_dict['case1'] = r_list[3]
                r_dict['case2'] = r_list[4]
                r_dict['case3'] = r_list[5]
                r_dict['case4'] = r_list[6]
                r_dict['case5'] = r_list[7]
                r_dict['case6'] = r_list[8]
                data_list.append(r_dict)


    print(data_list)
    return data_list

def renteDriver():
    chrome_path = "C:/Users/user/Downloads/chromedriver/chromedriver.exe"

    driver = webdriver.Chrome(chrome_path)
    # driver = webdriver.Chrome('/Users/user/Downloads/chromedriver_win32')
    ## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
    driver.implicitly_wait(3)

    driver.maximize_window()
    driver.get('http://finlife.fss.or.kr/annuitysaving/selectAnnuitySaving.do?menuId=2000107')
    driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[4]/div[2]/ul/li[2]/button').click()
    driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[4]/button').click()
    time.sleep(5)  # 5초 대기

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    table_rows = []
    for row in soup.select('#ajaxResult > div.table_area > table > tbody > tr'):
        table_rows.append([td.text.strip() for td in row.find_all('td')])

    data_list=[]
    for idx,rows in enumerate(table_rows):
        if idx % 2 == 0:
            r_list = [x for x in rows if x]
            if r_list:
                print(r_list)
                r_dict = {}
                r_dict['co_nm'] = r_list[1]
                r_dict['product_nm'] = r_list[2]
                r_dict['day'] = r_list[3]
                r_dict['count'] = r_list[4]
                r_dict['type'] = r_list[5]
                r_dict['y'] = r_list[6]
                r_dict['rate1'] = r_list[7]
                r_dict['rate2'] = r_list[8]
                r_dict['predict_yun'] = r_list[9]
                data_list.append(r_dict)


    print(data_list)
    return data_list

