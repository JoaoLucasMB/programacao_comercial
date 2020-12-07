import django_tables2 as tables
from .models import Veiculo

class VeiculoTable(tables.Table):
    class Meta:
        model = Veiculo
        template_name = "django_tables2/bootstrap.html"
        fields = ("Marca", "Modelo", "Ano Fabricação", "Modelo Fabricação", "Valor", "Combustível", )
        exclude = ("ID", )