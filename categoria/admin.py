from django.contrib import admin
from .models import Categoria
from django_markdown.admin import MarkdownModelAdmin


class CategoriaAdmin(MarkdownModelAdmin):
    pass

admin.site.register(Categoria, CategoriaAdmin)
