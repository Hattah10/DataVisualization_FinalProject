# Generated by Django 4.2.7 on 2023-11-20 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datavisualization_app', '0003_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dengue',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]