# Generated by Django 3.0.5 on 2020-04-06 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200406_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facts',
            name='facts_text_strong_numbers4',
        ),
    ]