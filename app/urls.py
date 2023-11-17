from django.urls import path
from app.views import *

app_name='nested-if'

urlpatterns = [
    path('condition/',condition,name='condition'),
]
