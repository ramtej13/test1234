# Generated by Django 3.0.5 on 2020-04-08 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20200408_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resuma_professional',
            name='resuma_professional_bullet4',
        ),
        migrations.RemoveField(
            model_name='resuma_professional',
            name='resuma_professional_bullet5',
        ),
        migrations.RemoveField(
            model_name='resuma_professional',
            name='resuma_professional_bullet6',
        ),
    ]