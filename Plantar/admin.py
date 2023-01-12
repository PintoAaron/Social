from django.contrib import admin
from django.contrib.auth.models import Group,User
from  django.db.models import Count
from . import models




class ProfileInline(admin.StackedInline):
    model = models.Profile
    

class customUser(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]
    
    
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User,customUser)



@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user']
