# Generated by Django 3.0.5 on 2020-04-11 16:46

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_employmentdetail_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('koica_code', models.CharField(max_length=255)),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('is_active', models.BooleanField(verbose_name='Active')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DepartmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Department detail',
            },
        ),
        migrations.RemoveField(
            model_name='employmentdetail',
            name='antecedents',
        ),
        migrations.RemoveField(
            model_name='employmentdetail',
            name='countries',
        ),
        migrations.RemoveField(
            model_name='employmentdetail',
            name='employment',
        ),
    ]