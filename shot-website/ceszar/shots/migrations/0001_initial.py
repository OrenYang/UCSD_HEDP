# Generated by Django 3.2.5 on 2024-02-08 22:30

from django.db import migrations, models
import django.db.models.deletion
import shots.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liners', models.CharField(choices=[('double', 'double'), ('single', 'single')], default='single', max_length=20)),
                ('gas', models.CharField(max_length=20)),
                ('chemical_symbol', models.CharField(max_length=10)),
                ('pressure', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gas', models.CharField(max_length=20)),
                ('chemical_symbol', models.CharField(max_length=10)),
                ('pressure', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('shot_num', models.IntegerField(blank=True, null=True)),
                ('current', models.FloatField(blank=True, null=True)),
                ('liners', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shots.liner')),
                ('target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shots.target')),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostic', models.CharField(choices=[('xuv', 'xuv'), ('schlieren', 'schlieren'), ('other', 'other')], default='other', max_length=20)),
                ('comments', models.TextField(null=True)),
                ('image', models.ImageField(upload_to=shots.models.image_upload_dir)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shots.test')),
            ],
        ),
    ]
