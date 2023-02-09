'''
파일명:pybo_filter.py
설 명:빼기 필터
생성일:2023-02-03
생성자:ohsunghun
since 2023.01.09 Copyright (C) by KandJamg All right reserved
'''

from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def mark(value):
    '''입력된 문자열을 html로 변환'''
    #nl2br(줄바꿈 문자-><dr>,fenced_code ->
    extensions = ['nl2br','fenced_code']
    return mark_safe(markdown.markdown(value,extensions=extensions))




@register.filter
def sub(value, arg):
    return value - arg
