# Generated by Django 3.1.6 on 2021-02-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20210225_0650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='company_state',
            new_name='company_satate',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='digital_signature',
            new_name='company_signature',
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_gst_type',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='compony',
            name='company_id',
            field=models.CharField(default='f24829e2', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unique_id',
            field=models.CharField(default='f0842642', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='pdf',
            field=models.FileField(upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='taxgroup',
            name='hsn_user_id',
            field=models.CharField(default='4b543ae7', max_length=150),
        ),
    ]
