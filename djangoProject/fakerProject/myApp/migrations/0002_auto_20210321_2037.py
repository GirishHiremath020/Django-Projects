# Generated by Django 3.0 on 2021-03-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ph',
            field=models.CharField(max_length=10),
        ),
    ]
