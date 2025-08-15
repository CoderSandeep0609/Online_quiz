from django.contrib import admin

from .models import *

@admin.register(DjangoQues)
class disp(admin.ModelAdmin):
    list_display=['id','question','option_a', 'option_b', 'option_c', 'option_d', 'correct_answer']

@admin.register(PythonQues)
class disp(admin.ModelAdmin):
    list_display=['id','question','option_a', 'option_b', 'option_c', 'option_d', 'correct_answer']

@admin.register(JavaQues)
class disp(admin.ModelAdmin):
    list_display=['id','question','option_a', 'option_b', 'option_c', 'option_d', 'correct_answer']

@admin.register(CppQues)
class disp(admin.ModelAdmin):
    list_display=['id','question','option_a', 'option_b', 'option_c', 'option_d', 'correct_answer']

