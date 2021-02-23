# Generated by Django 3.1.6 on 2021-02-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compony_name', models.CharField(max_length=150)),
                ('comapny_address', models.CharField(max_length=150)),
                ('company_city', models.CharField(max_length=150)),
                ('company_location', models.CharField(max_length=150)),
                ('company_pin', models.CharField(max_length=150)),
                ('company_district', models.CharField(max_length=150)),
                ('company_satate', models.CharField(max_length=150)),
                ('company_gstin', models.CharField(max_length=150)),
                ('company_email', models.CharField(max_length=150)),
                ('company_phone', models.CharField(max_length=150)),
                ('company_logo', models.TextField()),
                ('company_signature', models.CharField(max_length=150)),
                ('company_admin', models.CharField(max_length=150)),
                ('company_id', models.CharField(default='e042e834', max_length=150)),
            ],
        ),
    ]
