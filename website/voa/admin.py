from django.contrib import admin
#from .models import Question
from .models import *

# Register your models here.

class EstacoesAdmin(admin.ModelAdmin):
	list_display = ('nome','lat','lon')
	search_fields = ('nome','lat','lon')
admin.site.register(Estacoes,EstacoesAdmin)

class CampanhasAdmin(admin.ModelAdmin):
        list_display = ('nome','datai','dataf','descricao')
        search_fields = ('nome','datai','dataf','descricao')
admin.site.register(Campanhas,CampanhasAdmin)

class EquipamentosAdmin(admin.ModelAdmin):
        list_display = ('nome','descricao')
        search_fields = ('nome','descricao')
admin.site.register(Equipamentos,EquipamentosAdmin)

class MedicoesAdmin(admin.ModelAdmin):
        list_display = ('nome','estacao','campanha','equipamento','data')
        search_fields = ('nome','estacao','campanha','equipamento','data')
admin.site.register(Medicoes,MedicoesAdmin)

class CetaceosAdmin(admin.ModelAdmin):
        list_display = ('especie','data', 'lat', 'lon', 'prof', 'nindiv')
        search_fields = ('especie','data', 'lat', 'lon', 'prof', 'nindiv')
admin.site.register(Cetaceos,CetaceosAdmin)

class MergulhosAdmin(admin.ModelAdmin):
        list_display = ('data','estacao', 'fotos')
        search_fields = ('data','estacao', 'fotos')
admin.site.register(Mergulhos,MergulhosAdmin)
