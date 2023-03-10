'''
파일명:urls.py
설 명:
생성일:2023-01-27
생성자:ohsunghun
since 2023.01.09 Copyright (C) by KandJamg All right reserved
'''


from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),

    path('question/create/', views.question_create, name='question_create'),



    #temp menu
    path('boot/menu',views.boot_menu,name='boot_menu'),
    #bootstrap template
    path('boot/list',views.boot_list,name='boot_list'),
    path('boot/reg',views.boot_reg,name='boot_reg')


]