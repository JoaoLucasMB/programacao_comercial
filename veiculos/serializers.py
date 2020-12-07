# -*- coding: utf-8 -*-
from rest_framework import serializers
from veiculos.models import Veiculo

class SerializadorVeiculo(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        exclude = ['marca', 'modelo', 'valor']