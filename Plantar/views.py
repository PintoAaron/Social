from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('HELLO GUYS')


def home(request):
    return render(request,'home.html',{})