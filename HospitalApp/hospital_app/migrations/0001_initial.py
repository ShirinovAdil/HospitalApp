# Generated by Django 3.0.6 on 2020-05-05 14:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import hospital_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('address', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Specialities',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('birthdate', models.DateTimeField()),
                ('phone', models.CharField(help_text='Number in +994 format', max_length=13, validators=[django.core.validators.MinLengthValidator(13), hospital_app.models.number_validate])),
                ('email', models.EmailField(max_length=254)),
                ('registration_date', models.DateTimeField(help_text='You will be contacted for the exact time', verbose_name='Registration date to the doctor')),
                ('complaint', models.TextField(blank=True, verbose_name='Complaint/Comment')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.Speciality')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.Hospital')),
            ],
        ),
    ]
