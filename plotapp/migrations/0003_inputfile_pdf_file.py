# Generated by Django 3.0 on 2019-12-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotapp', '0002_inputfile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputfile',
            name='pdf_file',
            field=models.FileField(null=True, upload_to='', verbose_name='Input File'),
        ),
    ]
