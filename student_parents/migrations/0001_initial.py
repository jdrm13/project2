# Generated by Django 3.2.5 on 2021-10-01 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import student_parents.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_standard', models.CharField(choices=[('UKG', 'UKG'), ('LKG', 'LKG'), ('PLG', 'Play Group'), ('NRS', 'Narsery'), ('1', 'Class 1'), ('2', 'Class 2'), ('3', 'Class 3'), ('4', 'Class 4'), ('5', 'Class 5'), ('6', 'Class 6'), ('7', 'Class 7'), ('8', 'Class 8'), ('9', 'Class 9'), ('10', 'Class 10'), ('11', 'Class 11'), ('12', 'Class 12')], max_length=3)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('N', "Dosn't Want to Specify"), ('M', 'Male'), ('F', 'Female')], default='N', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Child',
            },
        ),
        migrations.CreateModel(
            name='CommonForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_number', models.CharField(max_length=12, null=True)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3)),
                ('religion', models.CharField(choices=[('hinduism', 'Hinduism'), ('sikhism', 'Sikhism'), ('islam', 'Islam'), ('christianity', 'Christianity'), ('zoroastrianism', 'Zoroastrianism'), ('buddhism', 'Buddhism'), ('jainism', 'Jainism')], max_length=100)),
                ('category', models.CharField(choices=[('GENERAL', 'GENERAL'), ('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC')], max_length=100)),
                ('minority', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('aadhar_no', models.CharField(max_length=12, validators=[student_parents.models.CommonForm.validate_digit_length])),
                ('single_child', models.BooleanField(default=False)),
                ('adopted_child', models.BooleanField(default=False)),
                ('orphan_child', models.BooleanField(default=False)),
                ('child_with_needs', models.BooleanField(default=False)),
                ('current_address_line_1', models.CharField(max_length=100)),
                ('current_address_line_2', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('permanent_address_line_1', models.CharField(max_length=100)),
                ('permanent_address_line_2', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_state', models.CharField(max_length=100)),
                ('permanent_city', models.CharField(max_length=100)),
                ('permanent_pincode', models.CharField(max_length=6)),
                ('fathers_name', models.CharField(max_length=100, null=True)),
                ('fathers_dob', models.DateField(blank=True, null=True)),
                ('fathers_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('mothers_name', models.CharField(max_length=100, null=True)),
                ('mothers_dob', models.DateField(blank=True, null=True)),
                ('mothers_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True)),
                ('alternate_phone_no', models.CharField(blank=True, max_length=15, null=True)),
                ('family_annual_income', models.PositiveIntegerField(default=0)),
                ('privious_school', models.CharField(blank=True, max_length=100, null=True)),
                ('transfer_certificate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('fee_waiver_category', models.CharField(blank=True, max_length=100, null=True)),
                ('route_code', models.CharField(blank=True, max_length=100, null=True)),
                ('shift', models.CharField(blank=True, max_length=100, null=True)),
                ('stoppage_name', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='documents')),
                ('id_proof', models.FileField(blank=True, null=True, upload_to='documents')),
                ('caste_certificate', models.FileField(blank=True, null=True, upload_to='documents')),
                ('domicile', models.FileField(blank=True, null=True, upload_to='documents')),
                ('transfer_certificate', models.FileField(blank=True, null=True, upload_to='documents')),
                ('character_certificate', models.FileField(blank=True, null=True, upload_to='documents')),
                ('child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student_parents.child')),
            ],
        ),
    ]
