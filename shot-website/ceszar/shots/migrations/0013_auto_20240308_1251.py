# Generated by Django 3.2.5 on 2024-03-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0012_auto_20240308_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filter',
            old_name='filter',
            new_name='mat',
        ),
        migrations.AddField(
            model_name='filter',
            name='thickness',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
