# Generated by Django 3.2.3 on 2021-05-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='about',
            field=models.TextField(default='-'),
        ),
    ]
