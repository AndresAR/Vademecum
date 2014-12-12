# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

# Creacion Modelo Farmaco


class Farmaco(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField()
    # clasificacion = models.ForeignKey('Categoria')
    # propiedades farmacos
    accion_terapeutica = models.TextField()
    indicacion = models.TextField()
    posologia = models.TextField()
    efectos_colaterales = models.TextField()
    presentacion = models.TextField()
    composicion = models.TextField()

    def __unicode__(self):
        return self.nombre

    # Creación de Slug a partir del nombre del farmaco
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Farmaco, self).save(*args, **kwargs)
