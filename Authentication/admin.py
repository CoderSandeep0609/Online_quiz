from django.contrib import admin
from .models import *

@admin.register(StudentProfile)
class disp(admin.ModelAdmin):
    list_display=['id','user','first_name', 'last_name', 'gender', 'age', 'qualification', 'marks']


class Disp(admin.ModelAdmin):
    list_display=['id','user','subject','marks_obtained','total_marks']

admin.site.register(ExamData,Disp)
    
    