from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=80)
    roll_number = models.CharField(max_length=10)
    birth_date = models.DateField()
    joining_date = models.DateField()

    class Meta:
        db_table = "student"
