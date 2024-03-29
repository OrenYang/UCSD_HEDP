# Generated by Django 3.2.5 on 2024-02-09 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0004_remove_gasconfig_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasconfig',
            name='inner_press',
        ),
        migrations.RemoveField(
            model_name='gasconfig',
            name='inner_timing',
        ),
        migrations.RemoveField(
            model_name='gasconfig',
            name='outer_press',
        ),
        migrations.RemoveField(
            model_name='gasconfig',
            name='outer_timing',
        ),
        migrations.RemoveField(
            model_name='gasconfig',
            name='taget_press',
        ),
        migrations.RemoveField(
            model_name='gasconfig',
            name='target_timing',
        ),
        migrations.AddField(
            model_name='test',
            name='inner_press',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='inner_timing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='outer_press',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='outer_timing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='taget_press',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='target_timing',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
