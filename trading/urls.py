from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.trdaing_base, name='trading_base'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('gap_up', views.gap_up, name="gap_up"),
    path("gap_down", views.gap_down, name='gap_down'),
    path('red_green_red', views.red_green_red, name='red_green_red'),
    path('live_data', views.live_data, name='live_data'),
    path('login', views.login, name="login"),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('blog', views.blog, name='blog'),
    path('blog_post/<id>', views.blog_post, name='blog_post'),
    path('historic_data', views.historic_data, name='historic_data'),
    path('historic_data_view', views.historic_data_view, name='historic_data_view'),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# <file_name_id>