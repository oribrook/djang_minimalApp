from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):

    class Status(models.TextChoices):
        wait = 'wait'
        processing = 'processing'
        done =  'done'

    title = models.CharField(max_length=20, null=False, blank=False)
    content = models.CharField(max_length=200, null=False, blank=False)
    status = models.CharField(choices=Status.choices,  default=Status.wait, max_length=10)    
