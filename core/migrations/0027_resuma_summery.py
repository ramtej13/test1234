# Generated by Django 3.0.5 on 2020-04-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20200408_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resuma_summery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resuma_summery_name', models.TextField()),
                ('resuma_summery_paragraph', models.TextField(blank=True)),
                ('resuma_summery_bullet1', models.TextField(blank=True)),
                ('resuma_summery_bullet2', models.TextField(blank=True)),
                ('resuma_summery_bullet3', models.TextField(blank=True)),
            ],
        ),
    ]