from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms import ModelForm
from django import forms
from django.db.models import Max
from .models import Enquete, Opcao
from .forms import VotoForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages


@login_required
def listagem(request):
    data = {}
    data['enquetes'] = Enquete.objects.all
    data['Opcao'] = Opcao.objects.all

    def get_context_data(self, **kwargs):
        context = super(listagem, self). get_context_data(**kwargs)
        question = kwargs.get('object')
        context['totalVotos'] = question.VotosTotais()
        return super().get_context_data(**kwargs)

    return render(request , 'usuarios/enquetes.html' , data)
    

class EnqueteForm(ModelForm):
   class Meta:
        model = Enquete
        fields = ['titulo', 'descricao', 'data_inicio' , 'data_fim'] 
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título da Enquete', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descrição da Enquete', 'class': 'form-control'}),
            'data_inicio': forms.DateTimeInput(attrs={'placeholder': 'Data de Início', 'class': 'form-control', 'type': 'datetime-local'}),
            'data_fim': forms.DateTimeInput(attrs={'placeholder': 'Data de Fim', 'class': 'form-control', 'type': 'datetime-local'}),
        }

def forms(request):
    data = {}
    form = EnqueteForm(request.POST or None)

    if request.method == "POST":
        if 'save_enquete' in request.POST:  
            if form.is_valid():
                form.save()
                return redirect('Enquete')  
        elif 'add_opcoes' in request.POST:  
            if form.is_valid():
                enquete = form.save()  
                return redirect('enqueteopcoes', enquete.id) 

    data['form'] = form
    return render(request, 'usuarios/newEnquete.html', data)


def updateEnquete(request, pk):
    data = {}
    enquete = Enquete.objects.get(pk=pk)
    form = EnqueteForm(request.POST or None, instance=enquete)

    if form.is_valid():
        form.save()
        return redirect('Enquete')

    data['form'] = form
    data['enquete'] = enquete
    return render(request, 'usuarios/newEnquete.html', data)
    
def deleteEnquete(request, pk):
    data = {}
    enquete = Enquete.objects.get(pk=pk)
    enquete.delete()
    return redirect('Enquete')

class opacaoForm(ModelForm):
   class Meta:
        model = Opcao
        fields = ['opcao']

def opcoesEnquete(request, pk=None):
    data = {}
    enquete = Enquete.objects.get(pk=pk)
    form = opacaoForm(request.POST or None, instance=Opcao)

    if request.method == 'POST':
        opcoes_data = request.POST.getlist('opcao')  
        
        opcao = [
            Opcao(enquete=enquete, opcao=opcao_texto)  
            for opcao_texto in opcoes_data
        ]

        Opcao.objects.bulk_create(opcao)
        return redirect('Enquete')
    
    data['form'] = form
    data['Opcao'] = enquete
    return render(request, 'usuarios/opcoes.html', data)   

def voto(request , pk):
    enquete = Enquete.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            selected_opcao = enquete.opcao_set.get(pk=request.POST['opcao'])
        except KeyError:
            print('Erro: Chave "opcao" não encontrada em request.POST')
            messages.error(request, 'Selecione uma alternativa para votar')
        except Opcao.DoesNotExist:
            print('Erro: Opcao com o pk especificado não existe para esta enquete') 
        else:
            selected_opcao.votos += 1
            selected_opcao.save()
            return redirect(  reverse_lazy ('Enquete'))
    
    data = {'question':  Enquete}
    return render(request, 'usuarios/enquetes.html', data)

def resultado(request , pk):
    enquete = Enquete.objects.get(pk=pk)
    data = {'enquete' : Enquete}
    data['votos'] = enquete.resultados()    

    return render(request, 'usuarios/resultado.html', data )