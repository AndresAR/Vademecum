from django.contrib import admin
from .models import Categoria
from django_markdown.admin import MarkdownModelAdmin

@admin.register(Categoria)
class CategoriaAdmin(MarkdownModelAdmin):
    pass
