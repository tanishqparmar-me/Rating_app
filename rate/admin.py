from django.contrib import admin
from . models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')  

class display(admin.ModelAdmin):
    list_display = ('name', 'rate', 'message')  


admin.site.register(user,UserProfileAdmin)
admin.site.register(rating,display)