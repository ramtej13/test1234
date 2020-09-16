from django.urls import re_path

from . import consumer

from django.conf.urls import url


websocket_urlpatterns = url(r'ws/chart_room/(?P<room_name>\w+)/$', consumer.ChatConsumer)

