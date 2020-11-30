# from django.shortcuts import render
# from django.views.generic import View
# from veiculos.models import Veiculo

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from veiculos.models import Veiculo
from veiculos.forms import FormularioVeiculo
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class VeiculosList(ListView):
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculos/listar.html'

class VeiculosNew(CreateView):
    # View para a criação de novos veículos
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class VeiculosEdit(UpdateView):
    # View para a edição de veículos já cadastrados.
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class VeiculosDelete(DeleteView):
    # View para deletar veículos cadastrados
    model = Veiculo
    template_name = 'veiculos/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

# class VeiculosList(View):
#     def get(self, request):
#         contexto = {
#             'lista_veiculos': Veiculo.objects.all().order_by('marca')
#         }
#         return render(request, 'veiculos/listar.html', contexto)
