# Generated by Django 3.2.8 on 2021-10-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=80)),
                ('roll_number', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('joining_date', models.DateField()),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
