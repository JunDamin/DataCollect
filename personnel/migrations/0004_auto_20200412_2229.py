# Generated by Django 3.0.5 on 2020-04-12 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20200411_2143'),
        ('personnel', '0003_personnelreport_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnelinfo',
            old_name='personnel',
            new_name='personnel_type',
        ),
        migrations.AlterField(
            model_name='personnelreport',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='personnel', to='data.Department'),
        ),
    ]
