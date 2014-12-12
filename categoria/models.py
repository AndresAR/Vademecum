# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify


# Creación Modelo Categoria de Farmacos(clasificación)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    slug = models.SlugField(editable=False)

    def __unicode__(self):
        return self.nombre

    # Creación de Slug a partir del nombre de la Categoría
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)
