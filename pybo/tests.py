from django.test import TestCase

# Create your tests here.
import unittest
import datetime
import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Crawling(unittest.TestCase):
    def setUp(self):
        logging.info('setUp')

    def tearDown(self):
        pass


    def naver_stock(self):
        '''주식 크롤링'''
        url = 'https://finance.naver.com/item/main.naver?code=005380'
        for i in range(1,4,1):
            self.call


    @unittest.skip('cgv 정보 이미지')
    def test_cgv(self): #http://www.cgv.co.kr/movies/?lt=1&ft=0 --> cgv

        url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
        response = requests.get(url)
        print('response.status_code:{}'.format(response.status_code))
        if 200 == response.status_code:
            html=response.text

            soup=BeautifulSoup(html,'html.parser')
            title = soup.select('div.box-contents strong.title')

            reserve = soup.select('div.score strong.percent span')

            poster = soup.select('span.thumb-image img')

            for page in range(0,7,1):
                posterImg = poster[page]
                imgUrlPath = posterImg.get('src')
                print('title[page]:{},{},{}'.format(title[page].getText(),
                                                    reserve[page].getText(),
                                                    imgUrlPath))
                pass
        else:
            print('접속 오류 response.status_code:{}'.format(response.status_code))
    @unittest.skip('네이버 날씨')
    def test_weather(self):  # https://weather.naver.com/today/09545101 --> 네이버 날씨
        logging.info('test_weather')
        newDate=datetime.datetime.now()
        #yyyymmdd hh:mm
        newDate.strftime('"%Y-%m-%d %H:%M:S')
        print('='*35)
        print(newDate)
        print('=' * 35)

        naverWetherUrl = 'https://weather.naver.com/today/09545101'
        html = urlopen(naverWetherUrl)

        print('html:{}'.format(html))
        bsObject=BeautifulSoup(html,'html.parser')
        tmpes=bsObject.find('strong','current')
        print('서울 마포구 서교동 날씨:{}'.format(tmpes.getText()))

        print('test_weather')
        pass