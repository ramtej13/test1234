from django.db import models

from datetime import datetime
from ckeditor.fields import RichTextField,CKEditorWidget


class Portfolio(models.Model):
    trading_base_image = models.ImageField(upload_to='trading/trading_base')
    trading_base_caption = models.TextField()
    trading_base_sub_cap = models.TextField(blank=True)
    trading_base_discription = models.TextField()
    trading_base_date = models.DateTimeField(blank=True)
    def __str__(self):
        return self.trading_base_caption


class Gap_up(models.Model):
    gap_up_current_price = models.IntegerField(blank=True, null=True)
    gap_up_open = models.IntegerField(default=0,blank=True, null=True)
    gap_up_percentage = models.IntegerField(blank=True, null=True)
    gap_up_yesterday_high = models.IntegerField(blank=True, null=True)
    gap_up_yesterday_symbol = models.TextField(blank=True, null=True)
    gap_up_today_symbol = models.TextField(blank=True, null=True)
    gap_up_chat_zerodha = models.TextField(blank=True, null=True)
    gap_up_chat_marketmojo = models.TextField(blank=True, null=True)
    gap_up_chat_economictimes = models.TextField(blank=True, null=True)


class Gap_down(models.Model):
    gap_down_current_price = models.IntegerField(blank=True, null=True)
    gap_down_open = models.IntegerField(default=0,blank=True, null=True)
    gap_down_percentage = models.IntegerField(blank=True, null=True)
    gap_down_yesterday_low = models.IntegerField(blank=True, null=True)
    gap_down_yesterday_symbol = models.TextField(blank=True, null=True)
    gap_down_today_symbol = models.TextField(blank=True, null=True)
    gap_down_chat1_zerodha = models.TextField(blank=True, null=True)
    gap_down_chat_marketmojo = models.TextField(blank=True, null=True)
    gap_down_chat_economictimes = models.TextField(blank=True, null=True)


class Red_green_red(models.Model):
    red_green_red_current_price = models.IntegerField(blank=True, null=True)
    red_green_red_open = models.IntegerField(default=0,blank=True, null=True)
    red_green_red_percentage_change = models.IntegerField(blank=True, null=True)
    red_green_red_difference = models.IntegerField(blank=True, null=True)
    red_green_red_yesterday_high = models.IntegerField(blank=True, null=True)
    red_green_red_yesterday_symbol = models.TextField(blank=True, null=True)
    red_green_red_today_symbol = models.TextField(blank=True,null=True)
    red_green_red_chat_zerodha = models.TextField(blank=True, null=True)
    red_green_red_chat_marketmojo = models.TextField(blank=True, null=True)
    red_green_red_chat_economictimes = models.TextField(blank=True, null=True)



class Main_trading_base(models.Model):
    main_trading_base_main_heading = models.TextField()


class Live_data(models.Model):
    live_data_open = models.IntegerField(default=0,blank=True, null=True)
    live_data_percentage_change = models.TextField(default=0,blank=True, null=True)
    live_data_high = models.IntegerField(default=0,blank=True, null=True)
    live_data_low = models.IntegerField(default=0,blank=True, null=True)
    live_data_volume = models.IntegerField(default=0,blank=True, null=True)
    live_data_symbole = models.TextField(blank=True,null=True)
    live_data_ltp = models.IntegerField(default=0,blank=True, null=True)
    live_data_chat_zerodha = models.TextField(blank=True, null=True)
    live_data_chat_marketmojo = models.TextField(blank=True, null=True)
    live_data_chat_economictimes = models.TextField(blank=True, null=True)

class Blog_Post_steps(models.Model):
    steps = RichTextField()
    def __str__(self):
        return self.steps

class Blog_Post_catogory(models.Model):
    catogory = models.TextField(null=True)
    def __str__(self):
        return self.catogory


class Blog_post(models.Model):
    title = models.CharField(max_length=200,null=True)
    body = RichTextField()
    created_at = models.DateTimeField(blank=True,null=True)
    steps = models.ForeignKey(Blog_Post_steps,on_delete=models.CASCADE, null=True)
    catogory = models.ForeignKey(Blog_Post_catogory,on_delete=models.CASCADE, null=True)
    blog_image = models.ImageField(upload_to='trading/blog_image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="Posts"


class Historic_data(models.Model):
    Historic_data_open = models.IntegerField(default=0,blank=True, null=True)
    Historic_data_percentage_change = models.TextField(default=0,blank=True, null=True)
    Historic_data_high = models.IntegerField(default=0,blank=True, null=True)
    Historic_data_low = models.IntegerField(default=0,blank=True, null=True)
    Historic_data_volume = models.IntegerField(default=0,blank=True, null=True)
    Historic_data_symbole = models.TextField(blank=True,null=True)
    Historic_data_ltp = models.IntegerField(default=0,blank=True, null=True)

    def __str__(self):
        return self.Historic_data_ltp

    class Meta:
        verbose_name_plural="Posts"
