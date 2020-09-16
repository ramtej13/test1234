# Generated by Django 3.0.5 on 2020-04-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_facts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_skills', models.TextField()),
                ('skill_number1', models.TextField()),
                ('skill_number2', models.TextField()),
                ('skill_number3', models.TextField()),
                ('skill_number4', models.TextField()),
                ('skill_number5', models.TextField()),
                ('skill_number6', models.TextField()),
                ('skill_percentage_number1', models.IntegerField()),
                ('skill_percentage_number2', models.IntegerField()),
                ('skill_percentage_number3', models.IntegerField()),
                ('skill_percentage_number4', models.IntegerField()),
                ('skill_percentage_number5', models.IntegerField()),
                ('skill_percentage_number6', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='facts',
            name='main_facts',
            field=models.TextField(),
        ),
    ]