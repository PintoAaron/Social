from django.contrib import admin
from django.contrib.auth.models import Group,User
from . import models




class ProfileInline(admin.StackedInline):
    model = models.Profile
    #extra = 0
    #min_num = 1
    #max_num = 10
    

class customUser(admin.ModelAdmin):
    moedl = User
    fields = ['username']
    inlines = [ProfileInline]
    
    
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User,customUser)



@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user']
   