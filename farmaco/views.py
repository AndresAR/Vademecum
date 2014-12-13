from django.views import generic
from . import models


class FarmacoIndex(generic.ListView):
    queryset = models.Farmaco.objects.validado()
    template_name = "index.html"
    paginate_by = 10