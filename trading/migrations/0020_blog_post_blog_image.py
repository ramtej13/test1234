# Generated by Django 3.0.5 on 2020-05-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0019_auto_20200524_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='blog_image',
            field=models.ImageField(default=0, upload_to='trading/blog_image'),
            preserve_default=False,
        ),
    ]