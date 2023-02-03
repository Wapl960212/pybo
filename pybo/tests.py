from django.test import TestCase

# Create your tests here.
import unittest
import datetime
import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Crawling(unittest.TestCase):
    def setUp(self):
        self.brower = webdriver.Firefox(executable_path='C:/projects/mysite/geckodriver.exe')
        print('setup')
        pass

    def tearDown(self):
        logging.info('tearDown')
        #btn =self.brower.find_element(By.ID, 'submit_btn')
        pass

    @unittest.skip('cgv 정보 이미지')
    def test_naver(self):
        self.brower("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

        id_textinput = self.brower.find_element(By.ID,'id')
        id_textinput.send_keys('good_day')

        id_textinput = self.brower.find_element(By.ID, 'pw')
        id_textinput.send_keys('4321')

        id_login = self.brower.find_element(By.ID, 'log.login ')
        id_login.click()
        pass

        from pybo.models import Question
        from django.utils import timezone
        q = Question(subject='금요일 입니다.[%3d]' % i, content='즐거운 금용일!', create_date=timezone.now())
        q.save()
    @unittest.skip('cgv 정보 이미지')
    def test_selenium(self):
        #self.brower = webdriver.Firefox(executable_path='C:/projects/mysite/geckodriver')
        self.brower.get('http://192.168.55.136:8000/pybo/')
        print('self.brower.title:{}'.format(self.brower.title))
        self.assertIn('Pybo',self.brower.title)

        content_textarea=self.brower.find_element(By.ID,'content')
        content_textarea.send_keys('오늘은 즐거운 금요일')

        btn = self.brower.find_element(By.ID,'submit_btn')
        btn.click()
        pass
    @unittest.skip('cgv 정보 이미지')
    def test_zip(self):
        intergers =[1,2,3]
        letters =['a','b','c']
        floats =[4.0,8.0,10.0]
        zipped=zip(intergers,letters,floats)
        list_data =list(zipped)
        print('list_data:{}'.format(list_data))


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