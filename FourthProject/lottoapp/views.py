from django.shortcuts import render
import random

# Create your views here.
def home(request) :
    return render(request, 'lottoapp/home.html')

def result(request) :
    list = ('이민정','김서영','김정운','노은성',
    '김소은','문다연','박혜준','안현주',
    '김유진','장한빛','조원아','황서경',
    '오예림','강연우','박경나','이연수')
    partner = random.sample(list,2)
    return render(request, 'lottoapp/result.html', {'partner':partner})