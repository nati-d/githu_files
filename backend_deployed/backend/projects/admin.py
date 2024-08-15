from django.contrib import admin
from .models import *
# Register your models here.

class  ProjectAdmin(admin.ModelAdmin):
 
    list_display = ['project_name','description','start_date','end_date','created_by','created_at']
    search_fields = ['project_name']
     
admin.site.register(Project,ProjectAdmin)     

