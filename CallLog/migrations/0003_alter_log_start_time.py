# Generated by Django 4.1.6 on 2023-02-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CallLog', '0002_alter_log_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
