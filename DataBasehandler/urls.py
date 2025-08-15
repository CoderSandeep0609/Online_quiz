from django.urls import path
from . import views

urlpatterns = [
    path('load/',views.load_ques,name='load_ques'),
]
