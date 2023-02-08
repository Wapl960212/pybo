'''
파일명:base_views.py
설 명:
생성일:2023-02-08
생성자:ohsunghun
since 2023.01.09 Copyright (C) by KandJamg All right reserved
'''

import logging

import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..foms import QuestionForm, AnswerForm
from ..models import Question, Answer

#crtl+alt+o(alpa) : import정리

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

