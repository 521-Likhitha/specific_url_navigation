from django.urls import path
from app1.views import *
app_name='chatgpt'
urlpatterns=[
    path('chat1/',chat1,name='chat1'),
    path('chat2/',chat2,name='chat2'),
]
