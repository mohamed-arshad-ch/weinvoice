# Generated by Django 3.1.6 on 2021-02-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_auto_20210225_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compony',
            name='company_id',
            field=models.CharField(default='91f18445', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unique_id',
            field=models.CharField(default='c3426110', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taxgroup',
            name='hsn_user_id',
            field=models.CharField(default='41a4ae8a', max_length=150),
        ),
    ]