from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('form',views.form,name='form'),
]

