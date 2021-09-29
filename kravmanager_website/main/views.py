from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Aluno, Plano
from .forms import AlunoForm, BuscaForm, PlanoForm

def home(request):
    return render(request, 'home.html', {})

def lista_alunos(request):
    if request.POST:
        alunos = Aluno.objects.filter(nome__contains=request.POST['searched'].order_by('nome'))
    else:
        alunos = Aluno.objects.all().order_by('nome')
    return render(request, 'lista_alunos.html', {'alunos':alunos})

def add_aluno(request):
    submitted = False
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Aluno cadastrado com sucesso!'))
            return redirect('add-aluno')
        else:
            messages.success(request, ('ERRO no cadastro!'))
            return redirect('add-aluno')
    else:
        form = AlunoForm()
        form.fields['instrutor'].queryset = Aluno.objects.exclude(titulo='aluno')
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_aluno.html', {'form':form, 'submitted':submitted})

def add_plano(request):
    submitted = False
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Novo plano cadastrado com sucesso!'))
            return redirect('add-plano')
        else:
            messages.success(request, ('ERRO no cadastro!'))
            return redirect('add-plano')
    else:
        form = PlanoForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_plano.html', {'form':form, 'submitted':submitted})

def lista_planos(request):
    planos = Plano.objects.all()
    return render(request, 'lista_planos.html', {'planos':planos})

def update_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    form.fields['instrutor'].queryset = Aluno.objects.exclude(titulo='aluno')
    if form.is_valid():
        form.save()
        return redirect('lista-alunos')
    return render(request, 'update_aluno.html', {'aluno':aluno, 'form':form})

def show_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    alunos = Aluno.objects.filter(instrutor=aluno)
    return render(request, 'show_aluno.html', {'aluno':aluno, 'alunos':alunos})

def update_plano(request, id):
    plano = Plano.objects.get(pk=id)
    form = PlanoForm(request.POST or None, instance=plano)
    if form.is_valid():
        form.save()
        return redirect('lista-planos')
    return render(request, 'update_plano.html', {'plano':plano, 'form':form})

def delete_plano(request, id):
    plano = Plano.objects.get(pk=id)
    plano.delete()
    return redirect('lista-planos')

def delete_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    aluno.delete()
    return redirect('lista-alunos')

def busca_avancada(request):
    submitted = False
    form = BuscaForm()
    if request.method == 'POST':
        ativo = request.POST.get('ativo', False)
        form = BuscaForm(request.POST)
        if form.is_valid():
            if ativo:
                alunos = Aluno.objects.exclude(plano_assinado__nome='INATIVO')
            else:
                alunos = Aluno.objects.all()
            if not form.cleaned_data['nome_busca']:
                alunos = alunos.order_by('nome')                
            else:
                alunos = Aluno.objects.filter(nome__contains=form.cleaned_data['nome_busca']).order_by('nome')
            if form.cleaned_data['faixa']:
                alunos  = alunos.filter(faixa__contains=form.cleaned_data['faixa'])
            if form.cleaned_data['plano_assinado']:
                alunos  = alunos.filter(plano_assinado=form.cleaned_data['plano_assinado'])
            return render(request, 'lista_alunos.html', {'alunos':alunos})
        else:
            messages.success(request, ('ERRO na busca!'))
            return redirect('home')
    else:
        form = BuscaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'busca_avancada.html', {'form':form, 'submitted':submitted})

def relatorio(request):
    planos = Plano.objects.exclude(nome='INATIVO')
    total = 0
    for plano in planos:
            total = total + plano.calcRendimento()
    total = round(total, 2)
    return render(request, 'relatorio.html', {'planos':planos, 'total':total})