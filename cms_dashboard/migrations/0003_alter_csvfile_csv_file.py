# Generated by Django 3.2.5 on 2021-11-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_dashboard', '0002_auto_20211104_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='csv_file',
            field=models.FileField(upload_to='csv_files'),
        ),
    ]
