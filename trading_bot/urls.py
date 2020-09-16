
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about',views.about,name='about'),
    path('chart',views.chart,name='chart'),
    path('profile',views.profile,name='profile'),
    path('stock_data', views.stock_data, name='stock_data'),
    path('resumadownload', views.resumadownload, name='resumadownload'),
    path('thankyou',views.thankyou,name='thankyou')
]