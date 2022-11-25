from django.db import models

# Create your models here.

class TennisPlayer(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=15)
    retired = models.BooleanField(default=True)

    def __str__(self):
        return f'Nombre: {self.name} | Nacionalidad: {self.country} | Retirado: {self.retired}'