# Generated by Django 3.0.5 on 2020-04-25 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0011_auto_20200425_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gap_down',
            old_name='gap_down_chat_maeketmojo',
            new_name='gap_down_chat_marketmojo',
        ),
        migrations.RenameField(
            model_name='gap_up',
            old_name='gap_up_chat_maeketmojo',
            new_name='gap_up_chat_marketmojo',
        ),
        migrations.RenameField(
            model_name='live_data',
            old_name='live_data_chat_maeketmojo',
            new_name='live_data_chat_marketmojo',
        ),
        migrations.RenameField(
            model_name='red_green_red',
            old_name='red_green_red_chat_maeketmojo',
            new_name='red_green_red_chat_marketmojo',
        ),
    ]