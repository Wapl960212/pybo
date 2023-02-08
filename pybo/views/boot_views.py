'''
파일명:boot_views.py
설 명:
생성일:2023-02-08
생성자:ohsunghun
since 2023.01.09 Copyright (C) by KandJamg All right reserved
'''

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


#crtl+alt+o(alpa) : import정리

def crawling_cgv(request):

    url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
    response = requests.get(url)
    print('response.status_code:{}'.format(response.status_code))
    context = {}

    if 200 == response.status_code:
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select('div.box-contents strong.title')

        reserve = soup.select('div.score strong.percent span')

        poster = soup.select('span.thumb-image img')

        title_list = []
        reserve_list = []
        poster_list = []
        for page in range(0, 7, 1):
            posterImg = poster[page]
            imgUrlPath = posterImg.get('src')
            title_list.append(title[page].getText())
            reserve_list.append(reserve[page].getText())
            poster_list.append(imgUrlPath)
            print('title[page]:{},{},{}'.format(title[page].getText(),
                                                reserve[page].getText(),
                                                imgUrlPath))
            pass
        context = {'context':zip(title_list,reserve_list,poster_list)}
    else:
        print('접속 오류 response.status_code:{}'.format(response.status_code))

    return render(request, 'pybo/crawling_cgv.html', context)

def boot_menu(request):
    return render(request,'pybo/menu.html')

def boot_reg(request):
    return render(request,'pybo/reg.html')

def boot_list(request):
    return render(request,'pybo/list.html')


