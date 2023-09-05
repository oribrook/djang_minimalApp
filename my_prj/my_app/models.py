from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    content = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.content[:min(len(self.content), 10)]}"