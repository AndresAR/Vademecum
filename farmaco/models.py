# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from categoria.models import Categoria
from django_markdown.models import MarkdownField


class FarmacoQuerySet(models.QuerySet):
    def validado(self):
        return self.filter(valido=True)


class Farmaco(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)
    clasificacion = models.ForeignKey(Categoria)
    # propiedades farmacos
    accion_terapeutica = MarkdownField(blank=True)
    indicacion = MarkdownField(blank=True)
    posologia = MarkdownField(blank=True)
    efectos_colaterales = MarkdownField(blank=True)
    presentacion = MarkdownField(blank=True)
    composicion = MarkdownField(blank=True)
    valido = models.BooleanField(default=True)

    objects = FarmacoQuerySet.as_manager()

    def __unicode__(self):
        return self.nombre

    # Creación de Slug a partir del nombre del farmaco
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Farmaco, self).save(*args, **kwargs)
