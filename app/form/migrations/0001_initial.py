# Generated by Django 4.0 on 2021-12-16 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('capacity', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=200, unique=True)),
                ('faculties', models.ManyToManyField(to='form.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='FormApplierModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('university_other', models.CharField(max_length=100, null=True)),
                ('faculty_other', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('department_other', models.CharField(max_length=100, null=True)),
                ('academic_year', models.CharField(max_length=50)),
                ('first_preference', models.CharField(max_length=50)),
                ('second_preference', models.CharField(max_length=50)),
                ('is_interviewed', models.BooleanField(default=0)),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='form.faculty')),
                ('time_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='form.timeslot')),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='form.university')),
            ],
        ),
    ]
