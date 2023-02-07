from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils import timezone
from .models import Question
from .foms import QuestionForm, AnswerForm
from bs4 import BeautifulSoup

import requests
import logging
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='common:login')
def question_delete(request, question_id):
    logging.info('1.question_delete')
    logging.info('2.question_id:{}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request,'삭제 권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)

    question.delete() #삭제
    return redirect('pybo:index')


@login_required(login_url='common:login')
def question_modify(request, question_id):
    '''질문 수정 : login필수'''
    logging.info('1.question-modify')
    question = get_object_or_404(Question, pk=question_id)


    #권한체크
    if request.user != question.author:
        messages.error(request,'수정 권한이 없습니다.')
        return redirect('pybo:detail',question_id = question.id)

    if request.method == 'POST':
        logging.info('2.question_modify post')
        form = QuestionForm(request.POST,instance=question)

        if form.is_valid():
            logging.info('3.form.is_valid():{}'.format(form.is_valid()))
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect("pybo:detail",question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)

    pass



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
@login_required(login_url='common:login')#로그인이 되어있지 않으면 login페이지로 이동
def question_create(request):
    '''질문 등록'''
    logging.info('1.request.method:{}'.format(request.method))
    if request.method == 'POST':
        logging.info('2.question_create post')
        #저장
        form = QuestionForm(request.POST) #request.POST 데이터 (subject,content 자동 생성)
        logging.info('3.question_create post')
        # form(질문 등록)이 유요하면
        if form.is_valid():
            logging.info('4.form.is_valid():{}'.format((form.is_valid())))
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author =request.user

            logging.info('4.question.author:{}'.format(question.author))

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

@login_required(login_url='common:login')#로그인이 되어있지 않으면 login페이지로 이동
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
            answer.author =request.user


            logging.info('3.question.author:{}'.format(answer.author))

            answer.save() #최종 저장
            return redirect('pybo:detail',question_id=question.id)
    else:
        logging.info('1.else:{}')
        form = AnswerForm()

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

    page=request.GET.get('page','1')

    question_list = Question.objects.order_by('-create_date')

    paginator=Paginator(question_list,10)
    page_obj=paginator.get_page(page)

#    paginator.count : 전체
#   paginator.per_page: 계시물수
#    paginator.page_range:페이지 범위

#    number : 현제 페이지번호
#    previous_page_number:이전
#    next_page_number:다음 페이지
#    has_previous:이전
#    has_next:다음
#    start_index:이작
#    end_index:끝 인덱스

    context = {'question_list': page_obj}
    logging.info('question_list:{}'.format(page_obj))


    return render(request, 'pybo/question_list.html', context)

