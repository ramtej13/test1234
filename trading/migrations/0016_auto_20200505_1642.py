# Generated by Django 3.0.5 on 2020-05-05 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0015_auto_20200505_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Post_steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='steps',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trading.Blog_Post_steps'),
        ),
    ]