# Generated by Django 3.1.6 on 2021-03-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0020_auto_20210316_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='subscription_end',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='subscription_plan',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='subscription_start',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='subscription_status',
        ),
        migrations.AlterField(
            model_name='compony',
            name='company_id',
            field=models.CharField(default='c93d798f', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unique_id',
            field=models.CharField(default='bb466b0d', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taxgroup',
            name='hsn_user_id',
            field=models.CharField(default='0f3b1a6f', max_length=150),
        ),
        migrations.AlterField(
            model_name='units',
            name='name',
            field=models.CharField(default='9532772e', max_length=100),
        ),
        migrations.AlterField(
            model_name='units',
            name='short_name',
            field=models.CharField(default='8c774da8', max_length=100),
        ),
    ]
