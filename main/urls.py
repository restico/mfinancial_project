from django.urls import path
from main.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home_page')
]
