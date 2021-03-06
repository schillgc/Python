# Generated by Django 3.0.5 on 2020-06-04 19:15

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0008_institution_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='registered',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=125)),
                ('last_name', models.CharField(blank=True, max_length=125)),
                ('email_address_of_instructor', models.EmailField(blank=True, max_length=254)),
                ('phone_number_of_instructor', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Education.Credit')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Education.Institution')),
            ],
            options={
                'verbose_name': 'Teaching Instructor',
                'verbose_name_plural': 'Teaching Instructors',
            },
        ),
    ]
