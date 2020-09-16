from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import os
import chart_room.routing
import trading_bot.routing

# import chart_room.consumer
# import trading_bot.consumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter([trading_bot.routing.trading_bot_urlpatterns,chart_room.routing.websocket_urlpatterns
    ])),
})


# from django.conf.urls import url
#
# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(URLRouter([
#         url(r"ws/trading_bot/stock_data/$", trading_bot.consumer.DashConsumer),
#         url(r'ws/chart_room/(?P<room_name>\w+)/$', chart_room.consumer.ChatConsumer),
#     ])),
# })
