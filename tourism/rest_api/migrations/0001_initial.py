# Generated by Django 4.1.1 on 2022-09-30 13:17

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longtitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beautyTitle', models.CharField(default='пер. ', max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('other_titles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
                ('connect', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('add_time', models.DateTimeField()),
                ('level_winter', models.CharField(blank=True, choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=2)),
                ('level_summer', models.CharField(blank=True, choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=2)),
                ('level_autumn', models.CharField(blank=True, choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=2)),
                ('level_spring', models.CharField(blank=True, choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=2)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new', max_length=8)),
                ('coord_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_api.coords')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('id_parent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SprActivitiesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('fam', models.CharField(blank=True, max_length=30)),
                ('otc', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.BinaryField()),
                ('title', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pereval_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.perevaladded')),
            ],
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_api.users'),
        ),
    ]