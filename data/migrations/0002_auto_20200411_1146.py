# Generated by Django 3.0.5 on 2020-04-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='korean',
            field=models.CharField(max_length=255),
        ),
    ]
