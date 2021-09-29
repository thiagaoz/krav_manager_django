from django.db import models
from django.db.models import Count
from django.forms.models import construct_instance
#from django.contrib.auth.models import User

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    menor = models.BooleanField(default=False)
    data_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)
    cell = models.IntegerField(blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    ativo = models.BooleanField(default=True)
    faixa = models.CharField(max_length=20, blank=True, null=True)
    data_inscricao = models.DateField('Data de Inscrição', blank=True, null=True)
    horario = models.CharField(max_length=20, blank=True, null=True)
    titulo = models.CharField(max_length=20, blank=True, default='')
    instrutor = models.ForeignKey('self', blank = True, null=True, on_delete=models.SET_NULL)
    plano_assinado = models.ForeignKey('Plano', blank=True, null=True, on_delete=models.SET_NULL)
    nome_busca = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

class Plano(models.Model):
    nome = models.CharField(max_length=30, default='')
    valor = models.FloatField(default=0)
    taxa = models.FloatField(default=0)
    custo_operacao = models.FloatField(default=0)

    def __str__(self):
        return self.nome

    def numInscritos(self):
        num = Aluno.objects.filter(plano_assinado__nome=self.nome).count()
        return  num

    def calcRendimento(self):
         num_alunos = self.numInscritos()
         rendimento = num_alunos * ( self.valor * (100 - self.taxa)/100 - self.custo_operacao)
         return round(rendimento, 2)