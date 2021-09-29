from django import forms
from django.forms import ModelForm
from .models import Aluno, Plano

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno

        FAIXAS = [
            ('BRANCA','BRANCA'),
            ('AMARELA','AMARELA'),
            ('LARANJA','LARANJA'),
            ('VERDER','VERDE'),
            ('AZUL','AZUL'),
            ('MARROM', 'MARROM'),
            ('PRETA', 'PRETA'),
        ]

        TITULOS = [('aluno', 'Aluno'), ('Mon','Monitor'), ('Ins', 'Instrutor'), ('Prf', 'Professor'), ('M', 'Mestre')]

        fields = ('nome','faixa','titulo','plano_assinado','instrutor',)
        labels = {
            'nome': 'Nome',
            'faixa': 'Faixa', 
            'titulo': 'Titulo',
            'plano_assinado':'Plano',
            'instrutor': 'Instrutor',
        }

        widgets = {
			'nome': forms.TextInput(attrs={'class':'form-control','class':"col-5",'placeholder':'Nome Completo'}),
            'faixa': forms.Select(choices=FAIXAS, attrs={'class':"form-select",'class':"col-1",}),
            'titulo': forms.Select(choices=TITULOS, attrs={'class':"form-select",'class':"col-2",}),        
        }

        def __init__(self, *args, **kwargs):
            super(AlunoForm, self).__init__(*args, **kwargs)
            self.fields['instrutor'].queryset = Aluno.objects.exclude(titulo='aluno')


class PlanoForm(ModelForm):
    class Meta:
        model = Plano
        fields = ('nome', 'valor','taxa', 'custo_operacao',)
        labels = {
            'nome': 'Nome do Plano',
            'valor': 'Valor R$:',
            'taxa': 'Taxa de Operação (%)',
            'custo_operacao': 'Custo por Operação R$'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control','class':"col-2",}),
            'valor': forms.NumberInput(attrs={'class':'form-control','class':"col-1",}),
            'taxa': forms.NumberInput(attrs={'class':'form-control','class':"col-1", 'placeholder':'0'}),
            'custo_operacao': forms.NumberInput(attrs={'class':'form-control','class':"col-1", 'placeholder':'0'}),
        }

class BuscaForm(ModelForm):
    class Meta:
        model = Aluno
        
        FAIXAS_BUSCA = [
            ('','TODAS'),
            ('BRANCA','BRANCA'),
            ('AMARELA','AMARELA'),
            ('LARANJA','LARANJA'),
            ('VERDER','VERDE'),
            ('AZUL','AZUL'),
            ('MARROM', 'MARROM'),
            ('PRETA', 'PRETA'),
        ]

        fields = ('nome_busca','faixa','plano_assinado',)
        labels = {
            'nome_busca':'',
            'faixa':'Faixa',
            'plano_assinado':'Plano',
        }   
        widgets ={
            'nome_busca': forms.TextInput(attrs={'class':'form-control','class':"col-5",'placeholder':'Buscar por nome?'}),
            'faixa': forms.Select(choices=FAIXAS_BUSCA, attrs={'class':"form-select",'class':"col-1",}),
            'plano_assinado': forms.Select(attrs={'class':"form-select",'class':"col-3",}),
        }