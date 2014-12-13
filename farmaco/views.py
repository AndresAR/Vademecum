from django.views import generic
from django.shortcuts import render
from categoria.models import Categoria
from .models import Farmaco


def index(request):
    context_dict = {}
    try:
        category = Categoria.objects.all()
        farmaco = Farmaco.objects.all()
        context_dict['categoria'] = category
        context_dict['farmacos'] = farmaco
    except Categoria.DoesNotExist:
        pass

    return render(request, 'index.html', context_dict)
