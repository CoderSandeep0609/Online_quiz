from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class StudendProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=['first_name','last_name','gender','age','qualification','marks']
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last Name'}),
            'age':forms.NumberInput,
        }
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'gender':'Choose gender',
            'age':'Enter age',
            'qualification':'choose Qualiofication',
            'marks':'Enter marks',
        }
        
    def clean(self):
        cleaned_data=super().clean()
        age=self.cleaned_data.get('age')
        if age is not None and not (16 <= age <= 30):
            raise forms.ValidationError("You are not eligible, age must be between 16 and 30.")

        
        marks=self.cleaned_data.get('marks')
        if marks:
            if marks is not None and not (0 <= marks <= 100):
                raise forms.ValidationError("Marks must be between 0 and 100.")

        return cleaned_data


class SignupForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))
    class Meta:
        model=User
        fields=['username','email',]
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter Username'}),
            'password1':forms.PasswordInput(attrs={'placeholder':'Enter Password'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})



    
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class SetNewPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
