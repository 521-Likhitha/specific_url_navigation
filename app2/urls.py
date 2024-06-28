from django.urls import path
from app2.views import *
app_name='aitool'

urlpatterns=[
    path('ai/',ai,name='ai'),
    path('ai_tool/',ai_tool,name='ai_tool'),
]