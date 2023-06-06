from django.db import models

# Create your models here.

class Car(models.Model):
    car_type = models.CharField(max_length=20)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.car_type