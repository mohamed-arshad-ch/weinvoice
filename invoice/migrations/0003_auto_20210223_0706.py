# Generated by Django 3.1.6 on 2021-02-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_compony'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn_code', models.CharField(max_length=150)),
                ('hsn_sgst', models.CharField(max_length=150)),
                ('hsn_cgst', models.CharField(max_length=150)),
                ('hsn_sess', models.CharField(max_length=150)),
                ('hsn_others', models.CharField(max_length=150)),
                ('hsn_user_id', models.CharField(default='2e7777c3', max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='compony',
            name='company_id',
            field=models.CharField(default='aff35433', max_length=150),
        ),
    ]