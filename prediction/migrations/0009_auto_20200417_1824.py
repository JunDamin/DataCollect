# Generated by Django 3.0.5 on 2020-04-17 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0008_auto_20200417_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prediction',
            old_name='latest_report',
            new_name='latest_prediction',
        ),
    ]