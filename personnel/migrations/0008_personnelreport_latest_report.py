# Generated by Django 3.0.5 on 2020-04-16 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20200414_2234'),
        ('personnel', '0007_auto_20200414_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnelreport',
            name='latest_report',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='latest_report', to='data.Department'),
        ),
    ]