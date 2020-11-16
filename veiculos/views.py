# from django.shortcuts import render
# from django.views.generic import View
# from veiculos.models import Veiculo

from django.views.generic import ListView, CreateView
# from django.urls import reverse lazy
from veiculos.models import Veiculo
# from veiculos.forms import FormularVeiculo

# Create your views here.

class VeiculosList(ListView):
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculos/listar.html'

# class VeiculosList(View):
#     def get(self, request):
#         contexto = {
#             'lista_veiculos': Veiculo.objects.all().order_by('marca')
#         }
#         return render(request, 'veiculos/listar.html', contexto)
