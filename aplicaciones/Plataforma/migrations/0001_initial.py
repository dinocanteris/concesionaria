# Generated by Django 5.1.3 on 2024-11-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('patente', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('km', models.IntegerField()),
                ('tipo', models.CharField(max_length=1)),
                ('disponibilidad', models.CharField(max_length=1)),
            ],
        ),
    ]