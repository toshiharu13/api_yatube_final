# Generated by Django 3.1.6 on 2021-02-04 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
    ]
