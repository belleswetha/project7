from csk.views import *
from django.urls import path

app_name='anything'

urlpatterns=[
    path('Sachin/',Sachin,name='Sachin')
]