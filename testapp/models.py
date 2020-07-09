from django.db import models

# Create your models here.
class Course_table(models.Model):
    Course_Name=models.CharField(max_length=250)
    Faculty=models.CharField(max_length=250)
    class_date=models.DateField( )
    class_time=models.TimeField()
    Fee=models.FloatField()
    Duration=models.IntegerField()
