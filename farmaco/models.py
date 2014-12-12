from django.db import models

# Create your models here.
class Farmaco(models.Model):
    nombre = models.CharField(max_length=50)
    