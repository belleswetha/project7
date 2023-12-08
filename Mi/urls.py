from Mi.views import *
from django.urls import path

app_name='anything' 

urlpatterns=[
    path('Raina/', Raina, name='Raina')
]