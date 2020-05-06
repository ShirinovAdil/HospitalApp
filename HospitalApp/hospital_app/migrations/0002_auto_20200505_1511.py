# Generated by Django 3.0.6 on 2020-05-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='registration_date',
            field=models.DateField(help_text='You will be contacted for the exact time', verbose_name='Registration date to the doctor'),
        ),
    ]
