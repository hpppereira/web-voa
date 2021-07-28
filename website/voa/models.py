from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Estacoes(models.Model):
    nome = models.CharField("Nome da Estação",max_length=200)
    lat = models.FloatField("Latitude")
    lon = models.FloatField("Longitude")
    prof = models.CharField(max_length=4,verbose_name="Profundidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Estações'
        verbose_name_plural = 'Estações'

class Campanhas(models.Model):
    nome = models.CharField("Nome da Campanha", max_length=200)
    #estacao = models.ForeignKey(Estacao,verbose_name='Estação',on_delete=models.CASCADE)
    #csv = models.FileField(verbose_name="csv", upload_to='data/', blank=True, null=True)
    #prof = models.CharField(max_length=60,verbose_name="Profundidade")
    datai = models.DateField(verbose_name="Data inicial", blank=True, null=True)
    dataf = models.DateField(verbose_name="Data final", blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Campanhas'
        verbose_name_plural = 'Campanhas'

class Equipamentos(models.Model):
    nome = models.CharField("Nome do Equipamento", max_length=200)
    descricao = models.TextField("Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Equipamentos'
        verbose_name_plural = 'Equipamentos'

class Medicoes(models.Model):
    nome = models.CharField("Nome da Medição", max_length=200)
    estacao = models.ForeignKey(Estacoes, verbose_name='Estação', on_delete=models.CASCADE)
    campanha = models.ForeignKey(Campanhas, verbose_name='Campanha', on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamentos, verbose_name='Equipamento', on_delete=models.CASCADE)
    data = models.DateField(verbose_name="Data", blank=True, null=True)

    def __str__(self):
        return self.nome
        #return self.data

    class Meta:
        verbose_name = 'Medições'
        verbose_name_plural = 'Medições'

class Cetaceos(models.Model):
    data = models.DateTimeField(verbose_name="Data", blank=True, null=True)
    lat = models.FloatField("Latitude", blank=True, null=True)
    lon = models.FloatField("Longitude", blank=True, null=True)
    prof = models.FloatField("Profundidade", blank=True, null=True)
    especie = models.CharField("Espécie", max_length=200, blank=True, null=True)
    nindiv = models.IntegerField("Número de indivíduos", blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)

#    def __str__(self):
        #return self.nome

    class Meta:
        ordering = ["data"]
        verbose_name = 'Cetáceos'
        verbose_name_plural = 'Cetáceos'

class Mergulhos(models.Model):
    data = models.DateTimeField(verbose_name="Data", blank=True, null=True)
    estacao = models.ForeignKey(Estacoes, verbose_name='Estação', on_delete=models.CASCADE)
    # lat = models.FloatField("Latitude", blank=True, null=True)
    # lon = models.FloatField("Longitude", blank=True, null=True)
    # prof = models.FloatField("Profundidade", blank=True, null=True)
    fotos = models.CharField("Fotos", max_length=200, blank=True, null=True)
    # nindiv = models.IntegerField("Número de indivíduos", blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)

#    def __str__(self):
        #return self.nome

    class Meta:
        ordering = ["data"]
        verbose_name = 'Mergulhos'
        verbose_name_plural = 'Mergulhos'

#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')

#    def __str__(self):
#        return self.question_text

#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#    def __str__(self):
#        return self.choice_text

