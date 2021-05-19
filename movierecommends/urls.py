from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import movies_home, save_date_to_db

urlpatterns = [
    path('', movies_home, name='movies_home'),
    path('save', save_date_to_db , name='save to db')
]
