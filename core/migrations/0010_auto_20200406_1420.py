# Generated by Django 3.0.5 on 2020-04-06 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_facts_facts_text_strong_numbers4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='skill_number2',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill_number3',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill_number4',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill_number5',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill_number6',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill_percentage_number2',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill_percentage_number3',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill_percentage_number4',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill_percentage_number5',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill_percentage_number6',
        ),
    ]