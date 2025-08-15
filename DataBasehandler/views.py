from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
import json,os
from django.conf import settings
# Create your views here.
def load_ques(req):
    duplicacy=0
    file_path = os.path.join(settings.BASE_DIR, 'questions.json')
    with open(file_path,'r') as f:
        data=json.load(f)
        for record in data:
            # RECOED FOR DJANGO QUESTIONS------
            if record.get('subject')=='django':
                if not DjangoQues.objects.filter(question=record.get('question')):
                    dj=DjangoQues(question=record.get('question'),option_a=record.get("options")['A'],option_b=record.get("options")['B'],\
                                  option_c=record.get("options")['C'],option_d=record.get("options")['D'],\
                                    correct_answer=record.get('options').get(record.get('correct_option')))
                    dj.save()
                else:
                    duplicacy+=1
            # RECOED FOR PYTHON QUESTIONS------
            elif record.get('subject')=='python':
                if not PythonQues.objects.filter(question=record.get('question')):
                    py=PythonQues(question=record.get('question'),option_a=record.get("options")['A'],option_b=record.get("options")['B'],\
                                  option_c=record.get("options")['C'],option_d=record.get("options")['D'],\
                                    correct_answer=record.get('options').get(record.get('correct_option')))
                    py.save()
                else:
                    duplicacy+=1
            # RECOED FOR JAVA QUESTIONS------
            elif record.get('subject')=='java':
                if not JavaQues.objects.filter(question=record.get('question')):
                    jv=JavaQues(question=record.get('question'),option_a=record.get("options")['A'],option_b=record.get("options")['B'],\
                                  option_c=record.get("options")['C'],option_d=record.get("options")['D'],\
                                    correct_answer=record.get('options').get(record.get('correct_option')))
                    jv.save()
                else:
                    duplicacy+=1
            # RECOED FOR Cpp QUESTIONS------
            elif record.get('subject')=='cpp':
                if not CppQues.objects.filter(question=record.get('question')):
                    cp=CppQues(question=record.get('question'),option_a=record.get("options")['A'],option_b=record.get("options")['B'],\
                                  option_c=record.get("options")['C'],option_d=record.get("options")['D'],\
                                    correct_answer=record.get('options').get(record.get('correct_option')))
                    cp.save()
                else:
                    duplicacy+=1
    print(f'Duplicate queston not uploaded {duplicacy}')
                
    messages.success(req,f'question loaded--------- {duplicacy} questions duplicates')
    return HttpResponseRedirect('/user/profile/')

