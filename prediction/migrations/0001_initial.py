# Generated by Django 3.0.5 on 2020-04-11 06:59

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('report_date', models.DateField()),
                ('description', models.TextField()),
                ('action', models.TextField()),
                ('employment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prediction', to='data.Employment')),
                ('risk_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prediction', to='prediction.RiskLevel')),
                ('risk_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prediction', to='prediction.RiskType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]