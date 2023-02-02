from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils import timezone
from .models import Question
from .foms import QuestionForm, AnswerForm
from bs4 import BeautifulSoup

import requests
import logging


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
        context = {'title': title_list,'reserve':reserve_list,'poster':poster_list}
    else:
        print('접속 오류 response.status_code:{}'.format(response.status_code))

    return render(request, 'pybo/crawling_cgv.html', context)

def question_create(request):
    '''질문 등록'''
    print('1.request.method:{}'.format(request.method))
    if request.method == 'POST':
        print('2.question_create post')
        #저장
        form = QuestionForm(request.POST) #request.POST 데이터 (subject,content 자동 생성)
        print('3.question_create post')
        # form(질문 등록)이 유요하면
        if form.is_valid():
            print('4.form.is_valid():{}'.format((form.is_valid())))
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect("pybo:index")
    else:
        form =QuestionForm()
    context = {'form': form}
    return render(request,'pybo/question_form.html', context)

def boot_menu(request):
    return render(request,'pybo/menu.html')

def boot_reg(request):
    return render(request,'pybo/reg.html')

def boot_list(request):
    return render(request,'pybo/list.html')


def answer_create(request, question_id):
    '''답변등록'''
    print('answer_create question_id:{}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form =AnswerForm(request.POST)
        print('1.request.method:{}'.format(request.method))
        if form.is_valid():
            print('2.form.is_valid()'.format(form.is_valid()))
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save() #최종 저장
            return redirect('pybo:detail',question_id=question.id)
    else:
        return HttpResponseNotAllowed('Post 만 사능 합니다.')

    #form validation
    context = {'question':question,'form':form}
    return render(request,'pybo/question_detail.html',context)


def detail(request,question_id):

    print('1.question_id:{}'.format(question_id))
    #question=Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)

    print('2.question:{}'.format(question))
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)



def index(request):

    logging.info('index fp벨로출력')
    # print('index 에벨로출력')
    question_list = Question.objects.order_by('-create_date')

    context = {'question_list': question_list}
    logging.info('question_list:{}'.format(question_list))


    return render(request, 'pybo/question_list.html', context)

