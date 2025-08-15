from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import StudendProfileForm
from django.contrib.auth.models import User
from .models import StudentProfile,ExamData
from django.contrib.auth.forms import PasswordChangeForm
from exam_subject.models import Feedback
from django.contrib.auth.forms import SetPasswordForm


def register_user(req):
    if req.method == "POST":
        sf = SignupForm(req.POST)
        if sf.is_valid():
            if not User.objects.filter(email=sf.cleaned_data['email']).exists():
                sf.save()
                messages.success(req, "Account Registered")
                return HttpResponseRedirect("/user/log_in/")
            else:
                messages.error(req,'email alrady exists')
    else:
        sf = SignupForm()
    return render(req, "signup.html", {"sign_up": sf})


def log_in(req):
    if req.method == "POST":
        lf = LoginForm(req, data=req.POST)
        if lf.is_valid():
            un = lf.cleaned_data.get("username")
            psw = lf.cleaned_data.get("password")
            chk = authenticate(username=un, password=psw)
            if chk is not None:
                if not chk.is_superuser:
                    login(req, chk)
                    return HttpResponseRedirect("/user/profile/")
                else:
                    messages.warning(req, "You are not a student---")
        else:
            messages.error(req, "invalid id or password")
    else:
        lf = LoginForm()
    return render(req, "login.html", {"log_in": lf, "admin": False})


def admin_log_in(req):
    if req.method == "POST":
        lf = LoginForm(req, data=req.POST)
        if lf.is_valid():
            un = lf.cleaned_data.get("username")
            psw = lf.cleaned_data.get("password")
            chk = authenticate(username=un, password=psw)
            if chk is not None:
                if chk.is_superuser:
                    login(req, chk)
                    return HttpResponseRedirect("/user/profile/")
                else:
                    messages.warning(req, "You are not an Admin")
        else:
            messages.success(req, "invalid id or password")
    else:
        lf = LoginForm()
    return render(req, "login.html", {"log_in": lf, "admin": True})


def log_out(req):
    logout(req)
    messages.success(req, "User logged out successfully")
    return HttpResponseRedirect("/user/log_in")


def profile(req):
    if req.user.is_authenticated:
        try:
            sp=StudentProfile.objects.get(user=req.user)
        except StudentProfile.DoesNotExist:
            sp=None
        ed=ExamData.objects.filter(user=req.user)
        pass_total=0
        avg=0
        total=0
        for i in ed:
            avg+=i.marks_obtained
            total+=i.total_marks
            if (i.marks_obtained)>= i.total_marks//2:
                pass_total+=1
        try:
            avg=(avg/total)*100
        except ZeroDivisionError:
            avg=0
        record={'attempt':len(ed),'pass_total':pass_total,'avg':avg}
        return render(req, "profile.html",{'student_data':sp,'exm_data':ed,'record':record})
    else:
        messages.error(req, " You have to login")
        return HttpResponseRedirect("/user/log_in/")


def edit_profile(req, my_id):
    if req.user.is_authenticated:
        if not req.user.is_superuser:
            usr = User.objects.get(pk=my_id)
            try:
                sp = StudentProfile.objects.get(user=usr)
            except StudentProfile.DoesNotExist:
                sp = None

            if req.method == "POST":
                spf = StudendProfileForm(req.POST, instance=sp)
                if spf.is_valid():
                    instance=spf.save(commit=False)
                    instance.user=usr
                    instance.save()
                    messages.success(req,'Profile Updated------')
                    return HttpResponseRedirect('/user/profile/')
                else:
                    print(spf.errors)
            else:
                spf=StudendProfileForm(instance=sp)
            return render(req, "edit_profile.html", {"form": spf})
        else:
            messages.warning(req,'Do not mendatory,, You are an Admin')
            return HttpResponseRedirect('/user/profile/')
    else:
        messages.error(req,'unauthorized Access')
        return HttpResponseRedirect('/user/log_in/')



def change_password(req):
    if req.method=='POST':
        pcf=PasswordChangeForm(user=req.user, data=req.POST)
        if pcf.is_valid():
            pcf.save()
            return HttpResponseRedirect('/user/profile/')
    else:
        pcf=PasswordChangeForm(user=req.user)
    return render(req,'change_password.html',{'form':pcf})

def feed_back(req):
    # send feedback data to admin profiles,,,
    fdbk=Feedback.objects.all()
    return render(req,'feedback.html',{'feedback_list':fdbk})



def forget_password(req):
    if req.method=='POST':
        usr=req.POST.get('userid')
        em=req.POST.get('email')
        if User.objects.filter(username=usr,email=em).exists():
            usrid=User.objects.get(username=usr)
            req.session['reset_id']=usrid.id
            return HttpResponseRedirect('/user/set_password')
        else:
            messages.error(req,'UserId or email Not found')
    return render(req,'forgetpassword.html')


def set_password(req):
    user_id = req.session.get('reset_id')
    if not user_id:
        messages.error(req, 'Session expired')
        return HttpResponseRedirect('/user/reset-password')
    user = User.objects.get(id=user_id)
    if req.method == 'POST':
        form = SetPasswordForm(user, req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Password changed successfully!')
            del req.session['reset_id']
            return HttpResponseRedirect('/user/log_in')
    else:
        form = SetPasswordForm(user)
    return render(req, 'set_password.html', {'reset_form': form})


