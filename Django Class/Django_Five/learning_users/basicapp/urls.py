from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'basicapp'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]