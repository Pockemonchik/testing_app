from django.contrib import admin
from django.contrib import admin

from .models import *

class TestingAdmin(admin.ModelAdmin):
    list_display = [
       
        'name'
       
    ]
    list_filter = (
        'name',
    
        )
    search_fields = [
        'name',
        'description',
    ]



admin.site.register(Test, TestingAdmin) 

# Register your models here.
