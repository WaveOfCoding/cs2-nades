from django.views.generic import ListView
from .models import *


class IndexView(ListView):
    template_name = 'index.html'
    model = Map
    queryset = Map.objects.filter().order_by('title')
