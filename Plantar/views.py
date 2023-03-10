from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from.models import Profile,Plant
from .forms import PlantForm

def hello(request):
    return HttpResponse('HELLO GUYS')


def home(request):
    if request.user.is_authenticated:
        form = PlantForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                plant = form.save(commit = False)
                plant.user = request.user
                plant.save()
                messages.success(request,"Your Plant has being posted")
                return redirect('home')
                    
        plants= Plant.objects.all().order_by('-create_at')
        return render(request,'home.html',{'plants':plants,"form":form})
    else:
        plants= Plant.objects.all().order_by('-create_at')
        return render(request,'home.html',{'plants':plants})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user = request.user)
        context = {'profiles':profiles}
        return render(request,'profile_list.html',context)
    else:
        messages.success(request,"Please log in to view this Page")
        return redirect('home')
    
def profile(request,id):
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk = id)
        plants = Plant.objects.filter(user_id = id)
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "follow":
                current_user_profile.follows.add(profile)
            elif action == "unfollow":
                current_user_profile.follows.remove(profile)
            current_user_profile.save()
        context = {'profile':profile,'plants':plants}
        return render(request,'profile.html',context)
    else:
        messages.success(request,"Please log in to view this Page")
        return redirect('home')
    
        

