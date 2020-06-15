# Generated by Django 3.0.5 on 2020-06-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0010_auto_20200610_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='course_weighted_grade_point_average',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, verbose_name='Weighted Grade Point Average for Course'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='required_exam',
            field=models.CharField(blank=True, choices=[('AP', 'Advanced Placement'), ('CLEP', 'College Level Examination Program'), ('PLTW', 'Project Lead the Way')], max_length=4),
        ),
        migrations.AlterField(
            model_name='credit',
            name='subject',
            field=models.CharField(blank=True, choices=[('Capstone', 'Capstone'), ('Fine Arts', 'Fine Arts'), ('Language Arts', 'Language Arts'), ('Mathematics', 'Mathematics'), ('Outdoor Education', 'Outdoor Education'), ('Physical Education', 'Physical Education'), ('Religion', 'Religious Studies'), ('Science', 'Science'), ('Social Studies', 'Social Studies'), ('Technology', 'Technology'), ('World Languages', 'World Languages')], max_length=18),
        ),
    ]
