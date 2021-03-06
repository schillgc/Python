# Generated by Django 3.1.5 on 2021-03-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theanalyzer', '0008_auto_20210309_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.URLField(blank=True, verbose_name="Company Logo's URL"),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
