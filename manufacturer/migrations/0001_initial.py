# Generated by Django 3.2 on 2021-05-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year_of_start', models.DateTimeField()),
                ('logo', models.CharField(blank=True, max_length=9999)),
            ],
        ),
    ]
