# Generated by Django 3.2.15 on 2023-07-08 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0003_videocall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocall',
            name='report',
        ),
        migrations.RemoveField(
            model_name='videocall',
            name='report_type',
        ),
    ]
