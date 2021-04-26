from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title