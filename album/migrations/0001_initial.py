# Generated by Django 5.1.2 on 2024-11-21 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('rating', models.PositiveIntegerField()),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musician')),
            ],
        ),
    ]
