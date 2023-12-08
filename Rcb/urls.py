from Rcb.views import *
from django.urls import path

app_name='anything'

urlpatterns=[
    path('kohli/', kohli ,name='kohli')
]