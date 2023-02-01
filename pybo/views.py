from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Question
from .foms import QuestionForm


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
    print('answer_create question_id:{}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)

    question. answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question_id)


def detail(request,question_id):

    print('1.question_id:{}'.format(question_id))
    #question=Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)

    print('2.question:{}'.format(question))
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)



def index(request):
    print('index 에벨로출력')
    question_list = Question.objects.order_by('-create_date')

    context = {'question_list': question_list}
    print()
    return render(request, 'pybo/question_list.html', context)

