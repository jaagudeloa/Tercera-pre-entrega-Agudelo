# Generated by Django 5.1.3 on 2024-11-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolarVar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TempVar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherVar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='WindVar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]