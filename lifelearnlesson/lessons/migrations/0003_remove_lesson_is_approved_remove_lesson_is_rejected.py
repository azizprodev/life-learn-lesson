# Generated by Django 5.0.7 on 2024-08-06 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_lesson_is_approved_lesson_is_rejected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='is_rejected',
        ),
    ]
