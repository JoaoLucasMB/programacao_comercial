from django.urls import path
from veiculos import views
# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    path('', views.VeiculosList.as_view(), name='listar-veiculos'),
    path('novo/', views.VeiculosNew.as_view(), name='novo-veiculo'),
    path('<int:pk>/', views.VeiculosEdit.as_view(), name='editar-veiculo'),
    path('deletar/<int:pk>/', views.VeiculosDelete.as_view(), name='deletar-veiculo'),
    path('api/listar/', views.VeiculosListAPI.as_view(), name='api-listar-veiculo'),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)