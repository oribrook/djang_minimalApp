from django.db import models


class Person(models.Model):
    person_id = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20, null=True, blank=True)    

    def __str__(self):
        return self.name 


class Car(models.Model):
    car_type = models.CharField(max_length=20)
    cost = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    owner = models.ForeignKey("Person", on_delete=models.RESTRICT, 
        related_name="p_cars")


    def __str__(self):
        return f"{self.car_type} - {self.year}"
    

class Rent(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    car = models.ForeignKey("Car", on_delete=models.CASCADE)
    client = models.ForeignKey("Person", on_delete=models.CASCADE)
