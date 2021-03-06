# Generated by Django 3.1.6 on 2021-03-01 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0016_auto_20210227_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='f2baebc1', max_length=100)),
                ('short_name', models.CharField(default='ab18e7e0', max_length=100)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='compony',
            name='company_id',
            field=models.CharField(default='7c66c05c', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unique_id',
            field=models.CharField(default='30138a73', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taxgroup',
            name='hsn_user_id',
            field=models.CharField(default='87722f03', max_length=150),
        ),
    ]
