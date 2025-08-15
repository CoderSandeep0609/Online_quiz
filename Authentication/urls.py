from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register_user,name='register_user'),
    path('log_in/',views.log_in,name='log_in'),
    path('admin/log_in/',views.admin_log_in,name='admin_log_in'),
    path('log_out/',views.log_out,name='log_out'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/<int:my_id>/',views.edit_profile,name='edit_profile'),
    path('user/change_password',views.change_password,name='change_password'),
    path('admin/feedback',views.feed_back,name='feedback'),
    path('reset-password',views.forget_password,name='forget_password'),
    path('set_password',views.set_password,name='set_password'),
]