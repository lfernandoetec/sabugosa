from django.shortcuts import render
from django.views import generic
from .models import Produto

# Create your views here.

class IndexView(generic.ListView):
    model = Produto
    template_name = 'index.html'


class SobreView(generic.TemplateView):
    template_name = 'sobre.html'

class ContatoView(generic.TemplateView):
    template_name = 'contato.html'