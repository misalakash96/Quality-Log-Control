# Generated by Django 5.0.6 on 2024-05-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='source',
            field=models.CharField(max_length=50),
        ),
    ]
