# Generated by Django 3.1.6 on 2021-02-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_auto_20210225_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compony',
            name='company_id',
            field=models.CharField(default='7d751b73', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unique_id',
            field=models.CharField(default='fae631c1', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taxgroup',
            name='hsn_user_id',
            field=models.CharField(default='c1a6129e', max_length=150),
        ),
    ]