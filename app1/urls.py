from app1.views import *
from django.urls import path

app_name="mama"
urlpatterns=[
    path('sudheer/',sudheer,name='sudheer'),
]