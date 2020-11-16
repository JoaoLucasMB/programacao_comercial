from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User

class Autenticacao(View):
    def get(self, request):
        contexto = {
            'usuario': '',
            'senha': ''
        }
        return render(request, 'autenticacao.html', contexto)
