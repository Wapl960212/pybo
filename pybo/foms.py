'''
파일명:foms.py
설 명: html form 관리
생성일:2023-02-01
생성자:ohsunghun
since 2023.01.09 Copyright (C) by KandJamg All right reserved
'''

from django import forms
from pybo.models import Question, Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer

        fields = ['content']

        labels = {
            'content': '답변내용'
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model =Question

        fields = ['subject','content']

        labels ={
            'subject':'제목',
            'content':'내용',
        }
