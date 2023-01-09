from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from.models import Profile

def hello(request):
    return HttpResponse('HELLO GUYS')


def home(request):
    return render(request,'home.html',{})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user = request.user)
        context = {'profiles':profiles}
        return render(request,'profile_list.html',context)
    else:
        messages.success(request,"Please log in to view this Page")
        return redirect('home')
        

