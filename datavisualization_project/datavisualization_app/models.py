from django.db import models


class Dengue(models.Model):
    Location = models.CharField(max_length=100)
    Cases = models.PositiveIntegerField()
    Deaths = models.PositiveIntegerField()
    Date = models.DateField()
    Region = models.CharField(max_length=100)

    class Meta:
        db_table = "dengue_dataset"


class Education(models.Model):
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    education_level = models.CharField(max_length=50)
    institution_type = models.CharField(max_length=50)
    it_student = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    load_shedding = models.CharField(max_length=10)
    financial_condition = models.CharField(max_length=10)
    internet_type = models.CharField(max_length=20)
    network_type = models.CharField(max_length=10)
    class_duration = models.CharField(max_length=20)
    self_lms = models.CharField(max_length=10)
    device = models.CharField(max_length=20)
    adaptivity_level = models.CharField(max_length=50)

    class Meta:
        db_table = "education_dataset"
