# Generated by Django 3.0.5 on 2020-04-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20200412_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_content',
            name='table_chart',
            field=models.TextField(blank=True),
        ),
    ]