from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ['title','start','end','all_day']

admin.site.register(Event,EventAdmin)       
 

