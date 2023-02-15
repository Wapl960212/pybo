'''
파일명:question_views.py
설 명:
생성일:2023-02-08
생성자:ohsunghun
since 2023.01.09 Copyright (C) by KandJamg All right reserved
'''
import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..foms import QuestionForm
from ..models import Question


#crtl+alt+o(alpa) : import정리

@login_required(login_url='common:login')
def question_vote(request, question_id):
    logging.info('1.question_vote, question_id:{}'.format(question_id))
<<<<<<< HEAD
    question= get_object_or_404(Question, pk=question_id)

    #본인글은 못하게
    if request.user == question.author:
        messages.error(request,'본인이 작성한 글은 추천할수 없습니다.')
    else:
        question.voter.add(request.user)

    return redirect('pybo:detail',question_id=question.id)

    pass
=======
    question = get_object_or_404(Question, pk=question_id)

    #본인글은 추천못함
    if request.user == question.author:
        messages.error(request,'본인이 작성한글은 추천이 안됨')
    else:
        question.voter.add(request.user)

    return redirect('pybo:detail',question_id=question_id)
>>>>>>> efa7429a808fbbe21c0a51675073b5862a297294


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
