from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import logging

logger = logging.getLogger(__name__)

class Autenticacao(View):
    def get(self, request):
        contexto = {
            'usuario': '',
            'senha': ''
        }
        return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        usuario = request.POST.get('usuario',None)
        senha = request.POST.get('senha', None)

        logger.info('Usuário: {}'.format(usuario))
        logger.info('Senha: {}'.format(senha))

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return HttpResponse('Usuario autenticado com sucesso')
                return redirect('/veiculos')

            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo'})
        return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha incorretos'})
