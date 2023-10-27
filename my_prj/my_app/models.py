from django.db import models


class GeneralFile(models.Model):

    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/', 
                            )
    def __str__(self) -> str:
        return f"<GeneralFile: {self.title}>"