# Generated by Django 3.2.5 on 2024-02-09 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0003_auto_20240209_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasconfig',
            name='config',
        ),
    ]
