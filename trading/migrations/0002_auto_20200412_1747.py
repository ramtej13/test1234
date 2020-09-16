# Generated by Django 3.0.5 on 2020-04-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gap_down',
            name='gap_down_chat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_down',
            name='gap_down_current_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_down',
            name='gap_down_open',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gap_down',
            name='gap_down_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_down',
            name='gap_down_today_symbol',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_down',
            name='gap_down_yesterday_low',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_down',
            name='gap_down_yesterday_symbol',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_up',
            name='gap_up_chat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_up',
            name='gap_up_current_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_up',
            name='gap_up_open',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gap_up',
            name='gap_up_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_up',
            name='gap_up_today_symbol',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_up',
            name='gap_up_yesterday_high',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gap_up',
            name='gap_up_yesterday_symbol',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='red_green_red',
            name='red_green_red_chat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='red_green_red',
            name='red_green_red_current_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='red_green_red',
            name='red_green_red_difference',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='red_green_red',
            name='red_green_red_open',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='red_green_red',
            name='red_green_red_percentage_change',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='red_green_red',
            name='red_green_red_yesterday_high',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='red_green_red',
            name='red_green_red_yesterday_symbol',
            field=models.TextField(blank=True, null=True),
        ),
    ]
