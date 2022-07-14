from django.conf.urls import url, include
from django.contrib import admin
from app01 import views
from web.views import account

urlpatterns = [
    url(r'^register/$',account.register,name='register'),
    url(r'^send/sms/$', account.send_sms,name='SMS'),

]