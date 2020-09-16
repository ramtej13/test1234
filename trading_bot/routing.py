from django.urls import re_path
from django.conf.urls import url

from . import consumer

trading_bot_urlpatterns = url(r"ws/trading_bot/stock_data/$", consumer.DashConsumer)



