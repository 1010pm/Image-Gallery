# في ملف myapp/models.py
from django.db import models

class Image(models.Model):
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.description

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)