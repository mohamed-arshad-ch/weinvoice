# Generated by Django 3.1.6 on 2021-02-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compony',
            name='company_id',
            field=models.CharField(default='975b1259', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unique_id',
            field=models.CharField(default='8f593083', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taxgroup',
            name='hsn_user_id',
            field=models.CharField(default='0f857751', max_length=150),
        ),
    ]
