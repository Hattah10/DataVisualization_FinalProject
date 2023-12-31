# Generated by Django 4.2.7 on 2023-12-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dengue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Cases', models.PositiveIntegerField()),
                ('Deaths', models.PositiveIntegerField()),
                ('Date', models.DateField()),
                ('Region', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dengue_dataset',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('education_level', models.CharField(max_length=50)),
                ('institution_type', models.CharField(max_length=50)),
                ('it_student', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=10)),
                ('load_shedding', models.CharField(max_length=10)),
                ('financial_condition', models.CharField(max_length=10)),
                ('internet_type', models.CharField(max_length=20)),
                ('network_type', models.CharField(max_length=10)),
                ('class_duration', models.CharField(max_length=20)),
                ('self_lms', models.CharField(max_length=10)),
                ('device', models.CharField(max_length=20)),
                ('adaptivity_level', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'education_dataset',
            },
        ),
    ]
