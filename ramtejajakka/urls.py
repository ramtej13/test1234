from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('core.urls')),
    path('trading/',include('trading.urls')),
    path('chart_room/', include('chart_room.urls')),
    path('trading_bot/', include('trading_bot.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

