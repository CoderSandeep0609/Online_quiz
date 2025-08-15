from django.urls import path
from . import views

urlpatterns = [
    path('python_test/',views.python,name='python_test'),
    path('django_test/',views.django,name='django_test'),
    path('cpp_test/',views.cpp,name='cpp_test'),
    path('java_test/',views.java,name='java_test'),
    path('delete_exam_rec/<int:id>',views.delete_exam_rec,name='delete_exam')
]
