from django.contrib import admin
from .models import Portfolio,Main_trading_base, \
    Blog_post,Blog_Post_steps,Blog_Post_catogory


# Register your models here.

admin.site.register(Portfolio),
admin.site.register(Main_trading_base),
admin.site.register(Blog_post),
admin.site.register(Blog_Post_steps),
admin.site.register(Blog_Post_catogory),

