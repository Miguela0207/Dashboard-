from django.db import models

# Create your models here.

class Venta(models.Model):
    barrio = models.CharField(max_length=120)
    venta = models.IntegerField()
    mes = models.CharField(max_length=120)