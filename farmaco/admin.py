from django.contrib import admin
from .models import Farmaco
from django_markdown.admin import MarkdownModelAdmin

@admin.register(Farmaco)
class FarmacoAdmin(MarkdownModelAdmin):
    pass

