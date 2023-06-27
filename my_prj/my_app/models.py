from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import datetime as dt


class Article(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    published = models.DateField(default=timezone.now, editable=True)

    def __str__(self):
        return f"{self.title} - {self.published}"