# Generated by Django 5.1 on 2024-09-06 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=75, unique=True)),
                ('dept_code', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=75, unique=True)),
                ('course_code', models.CharField(max_length=25, unique=True)),
                ('dept_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department')),
            ],
            options={
                'unique_together': {('dept_code', 'course_code')},
            },
        ),
    ]
