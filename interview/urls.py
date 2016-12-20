'''
Created on Dec 20, 2016

@author: imosweu
'''

from django.conf.urls import url

from . import views

app_name = 'interview'
urlpatterns = [
    url(r'^$', views.index , name = 'index'),
    # ex: /interview/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    ]