# Generated by Django 3.2.3 on 2021-07-28 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.TextField(default=''),
        ),
    ]
