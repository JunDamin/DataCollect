# Generated by Django 3.0.5 on 2020-04-11 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20200411_2116'),
        ('personnel', '0002_auto_20200411_2116'),
        ('prediction', '0004_auto_20200411_2116'),
        ('events', '0006_auto_20200411_2116'),
        ('users', '0002_auto_20200411_2116'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employment',
        ),
        migrations.DeleteModel(
            name='EmploymentDetail',
        ),
        migrations.AddField(
            model_name='departmentdetail',
            name='antecedents',
            field=models.ManyToManyField(blank=True, related_name='antecedents', to='data.Department'),
        ),
        migrations.AddField(
            model_name='departmentdetail',
            name='countries',
            field=models.ManyToManyField(blank=True, related_name='department_detail', to='data.Country'),
        ),
        migrations.AddField(
            model_name='departmentdetail',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_detail', to='data.Department'),
        ),
    ]
