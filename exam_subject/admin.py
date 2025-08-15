from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(AttemptAnswer)
class display(admin.ModelAdmin):
    list_display=['id','user','subject','question','selected_answer','correct_answer','submitted_at']

@admin.register(Feedback)
class disp(admin.ModelAdmin):
    list_display=['id','user','fullname','email','subject','message']