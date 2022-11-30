from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=100, decimal_places=2)
    qrade = models.IntegerField()
    



# 2. создайте django проект с приложением school создайте модель student с полями first_name, last_name, age, grade