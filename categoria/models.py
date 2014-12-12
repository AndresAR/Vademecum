# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField


# Creación Modelo Categoria de Farmacos(clasificación)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = MarkdownField()
    slug = models.SlugField(editable=False)

    def __unicode__(self):
        return self.nombre

    # Creación de Slug a partir del nombre de la Categoría
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)
