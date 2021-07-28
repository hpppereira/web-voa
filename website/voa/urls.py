from django.urls import path

from . import views

app_name = 'voa'
urlpatterns = [
    path('', views.index, name='index'),
    path('veleiro/', views.veleiro, name='veleiro'),
    path('equipamentos/', views.equipamentos, name='equipamentos'),
    path('projetos/', views.projetos, name='projetos'),
    path('servicos/', views.servicos, name='servicos'),
    path('expedicoes/', views.expedicoes, name='expedicoes'),
    path('dados/', views.dados, name='dados'),
    path('dados/cetaceos/', views.cetaceos, name='cetaceos'),
    path('dados/mergulhos/', views.mergulhos, name='mergulhos'),
    ]


