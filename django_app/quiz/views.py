from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
# from django.views.generic import TemplateView
from .forms import AnswerForm
# Create your views here.

# def index(request):
#     params = {
#         'title':'クイズアプリ作成',
#         'msg': '大変',
#         'answer': 'わかるかな？',
#         'form': AnswerForm()
#     }
#     if(request.method == 'POST'):
#         params['title']='Formクラス使えている！'
#         params['msg']='年齢：'+request.POST['age']
#         params['answer']='正解は：'+request.POST['answer']
#         params['form'] = AnswerForm(request.POST)
#     return render(request,'quiz/index.html',params)

# class AnswerView(TemplateView):

#     def __init__(self):
#         self.params = {
#             'title':'クイズアプリ作成',
#             'msg': '大変',
#             'answer': 'わかるかな？',
#             'form': AnswerForm()
#         }
    
#     def get(self,request):
#         return render(request,'quiz/index.html',self.params)

#     def post(self,request):
#         self.params['title']='Formクラス使えている！'
#         self.params['msg']='年齢：'+request.POST['age']
#         self.params['answer']='正解は：'+request.POST['answer']
#         self.params['form'] = AnswerForm(request.POST)
#         return render(request,'quiz/index.html',self.params) 

def index(request):
    data=Quiz.objects.all()
    params = {
        'title':'IT_Cross_Word',
        'level':'初級',
        'horizontal':'',
        'vertical':'',
        'form':AnswerForm(),
        'quiz_img_src':'',
        'answer_img_src':'',
        'reply':'',
        'answer':'',
        'judge':'',
        'data':data,
    }
    item=Quiz.objects.get(id=1)
    params['quiz_img_src']=item.quiz_img_src
    params['horizontal']=item.horizontal
    params['vertical']=item.vertical
    if(request.method == 'POST'):
        item = Quiz.objects.get(id=1)
        ansform = request.POST['answer']
        answer = item.answer
        params['form'] = AnswerForm(request.POST)
        if(ansform==answer):
            params['answer_img_src']=item.answer_img_src
            params['judge']='正解⭕️'
            params['answer']=answer 
            params['reply']=ansform
        else:
            params['answer_img_src']=item.answer_img_src
            params['judge']='不正解❌'
            params['answer']=answer
            params['reply']=ansform
    return render(request,'quiz/index.html',params)

