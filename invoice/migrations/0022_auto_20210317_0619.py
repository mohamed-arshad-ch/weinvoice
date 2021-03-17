# Generated by Django 3.1.6 on 2021-03-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0021_auto_20210316_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirments', models.CharField(max_length=200)),
                ('status', models.CharField(default='pending', max_length=150)),
                ('delivary_date', models.DateField()),
                ('delivary_approved_date', models.DateField()),
                ('order_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='compony',
            name='company_id',
            field=models.CharField(default='7175d625', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unique_id',
            field=models.CharField(default='72a0f1d0', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taxgroup',
            name='hsn_user_id',
            field=models.CharField(default='f6b5e5dd', max_length=150),
        ),
        migrations.AlterField(
            model_name='units',
            name='name',
            field=models.CharField(default='7e8a5292', max_length=100),
        ),
        migrations.AlterField(
            model_name='units',
            name='short_name',
            field=models.CharField(default='6df16b71', max_length=100),
        ),
    ]