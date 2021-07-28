#from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
#from django.template import loader
#from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.urls import reverse

#from .models import Choice, Question
from .models import *

# Create your views here.

def index(request):
    return render(request, 'voa/index.html')

def veleiro(request):
    return render(request, 'voa/veleiro.html')

def projetos(request):
    return render(request, 'voa/projetos.html')

def servicos(request):
    return render(request, 'voa/servicos.html')

def equipamentos(request):
    return render(request, 'voa/equipamentos.html')

def expedicoes(request):
    return render(request, 'voa/expedicoes.html')

def dados(request):
    return render(request, 'voa/dados.html')

def cetaceos(request):
    cetaceos_tab = Cetaceos.objects.all().order_by('data')
    return render(request, 'voa/cetaceos.html', {"cetaceos_tab": cetaceos_tab})

def mergulhos(request):
    mergulhos_tab = Mergulhos.objects.all().order_by('data')
    return render(request, 'voa/mergulhos.html', {"mergulhos_tab": mergulhos_tab})
