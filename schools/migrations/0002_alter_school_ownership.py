# Generated by Django 3.2.5 on 2021-11-09 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='ownership',
            field=models.CharField(choices=[('UN', 'UNKNOWN'), ('PR', 'PRIVATE'), ('PRA', 'PRIVATE-AIDED')], default='UN', max_length=50),
        ),
    ]
