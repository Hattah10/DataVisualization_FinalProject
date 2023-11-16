from django.db import models

class Dengue(models.Model):  
    id = models.AutoField(primary_key=True)
    Location = models.CharField(max_length=100)  
    Cases = models.PositiveIntegerField() 
    Deaths = models.PositiveIntegerField()
    Date = models.DateField()
    Region = models.CharField(max_length=100) 
   
    class Meta:  
        db_table = "dengue_dataset"