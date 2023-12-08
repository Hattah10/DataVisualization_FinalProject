# Generated by Django 4.2.7 on 2023-11-20 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datavisualization_app', '0002_alter_dengue_id'),
    ]

    operations = [
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