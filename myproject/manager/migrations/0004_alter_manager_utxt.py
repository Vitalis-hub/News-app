# Generated by Django 3.2.3 on 2021-08-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_manager_utxt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='utxt',
            field=models.TextField(),
        ),
    ]
