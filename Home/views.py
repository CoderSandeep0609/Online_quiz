from django.shortcuts import render
from exam_subject.models import Feedback
from django.contrib import messages

def home(req):
    return render(req,'home.html')

def contact(req):
    if req.method=='POST':
        name=req.POST.get('name')
        email=req.POST.get('email')
        sub=req.POST.get('subject')
        msgs=req.POST.get('message')
        if not req.user.is_superuser:
            obj=Feedback(user=req.user,fullname=name,email=email,subject=sub,message=msgs)
            obj.save()
            messages.success(req,'FeedBack has been Send to the Admin.....')
        else:
            messages.error(req,'Admin are not able to give feedback')
    return render(req,'contact.html')