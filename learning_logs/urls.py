"""define url patterns for learning_logs"""
from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    #topics page
    path('topics/', views.topics, name='topics'),
    #detail page for single topic
    path('topics/<topic_text>/', views.topic, name='topic')
]


