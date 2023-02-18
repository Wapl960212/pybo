'''
파일명 : base_views.py
설 명 :
생성일 : 2023-02-14
생성자 : user
since 2023.01.09 Copyright (C) by KandJang All right reserved.
'''


import logging

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ..models import Board


def index(request):

    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    div = request.GET.get('div', '')  # 검색어구분
    size = request.GET.get('size', '10')  # 페이지 사이즈
    logging.info('page:{}'.format(page))
    logging.info('kw:{}'.format(kw))
    logging.info('div:{}'.format(div))
    logging.info('size:{}'.format(size))

    board_list = Board.objects.order_by('-create_date')  # order_by('-필드') desc, asc order_by('필드')

    if '10' == div:   #제목
        logging.info('if 10')
        board_list = board_list.filter(subject__contains=kw)
    elif '20' == div: #내용
        logging.info('elif 20')
        board_list = board_list.filter(content__contains=kw)
    elif '30' == div: #등록자
        logging.info('elif 30')
        board_list = board_list.filter(author__username__contains=kw)

    # paging
    paginator = Paginator(board_list, size)
    page_obj = paginator.get_page(page)


    context = {'board_list': page_obj, 'kw':kw, 'page':page,'div':div,'size':size}
    logging.info('board_list:{}'.format(board_list))

    return render(request, 'board/board_list.html', context)


def detail(request,board_id):
    logging.info('board_id:{}'.format(board_id))
    #board = Board.objects.get(id=board_id)

    board = get_object_or_404(Board, pk=board_id)
    context = {'board':board}
    logging.info('board:{}'.format(board))

    return render(request,'board/board_detail.html',context)












