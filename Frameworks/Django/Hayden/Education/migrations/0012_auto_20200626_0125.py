# Generated by Django 3.0.5 on 2020-06-26 05:25

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Education', '0011_auto_20200615_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='course_weighted_grade_point_average',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3,
                                      verbose_name='Weighted Grade Point Average (GPA) for Course'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='grade_level',
            field=models.CharField(
                choices=[('6th Grade', '6th Grade'), ('7th Grade', '7th Grade'), ('8th Grade', '8th Grade'),
                         ('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'),
                         ('Senior', 'Senior'), ('Graduate', 'Graduate School')], max_length=9,
                verbose_name='Grade Level'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='required_exam',
            field=models.CharField(blank=True,
                                   choices=[('AP', 'Advanced Placement'), ('CLEP', 'College Level Examination Program'),
                                            ('PLTW', 'Project Lead the Way')], max_length=4,
                                   verbose_name='Required Exam for College Credit'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='subject',
            field=models.CharField(blank=True, choices=[('Capstone', 'Capstone'), ('Fine Arts', 'Fine Arts'),
                                                        ('Language Arts', 'Language Arts'),
                                                        ('Mathematics', 'Mathematics'),
                                                        ('Outdoor Education', 'Outdoor Education'),
                                                        ('Physical Education', 'Physical Education'),
                                                        ('Religion', 'Religious Studies'), ('Science', 'Science'),
                                                        ('Social Studies', 'Social Studies'),
                                                        ('Technology', 'Technology'),
                                                        ('World Languages', 'World Languages')], max_length=18,
                                   verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='course',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Education.Credit',
                                    verbose_name='Name of School Credit'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='email_address_of_instructor',
            field=models.EmailField(blank=True, max_length=254, verbose_name="Instructor's Email Address"),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='first_name',
            field=models.CharField(blank=True, max_length=125, verbose_name="Instructor's First Name"),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='last_name',
            field=models.CharField(blank=True, max_length=125, verbose_name="Instructor's Last Name"),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='phone_number_of_instructor',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None,
                                                                 verbose_name="Instructor's Telephone Number"),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Education.Institution',
                                    verbose_name='School Name'),
        ),
    ]