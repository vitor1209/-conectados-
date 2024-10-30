from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse
from django.forms import ModelForm
from django import forms
from .models import Usuario
from .models import Enquete
from .models import Opcao
from .models import Enquete
from django.db.models import Max

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha'] 

def user(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Enquete')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/user.html' , {'form': form})

def listagem(request):
    data = {}
    data['enquetes'] = Enquete.objects.all
    data['Opcao'] = Opcao.objects.all
    return render(request , 'usuarios/enquetes.html' , data)

def listagem(request):
    data = {}
    data['enquetes'] = Enquete.objects.all
    data['Opcao'] = Opcao.objects.all
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

    if form.is_valid():
        form.save()
        return redirect('Enquete')

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
    if pk:
        data = {}
        enquete = get_object_or_404(Enquete, pk=pk)
        form = opacaoForm(request.POST or None, instance=Opcao)

        if request.method == 'POST':
            form = opacaoForm(request.POST) 
            if form.is_valid():
                opcao = form.save(commit=False)
                opcao.enquete = enquete
                opcao.save()
                return redirect('Enquete')
            else:
                return redirect('Enquete')
        data['form'] = form
        data['Opcao'] = enquete
        return render(request, 'usuarios/opcoes.html', data)       

    else:
        data = {}
        maior_id = Enquete.objects.aggregate(Max('id'))['id__max']
        enquete = (maior_id or 0) + 1

        form = opacaoForm(request.POST or None, instance=Opcao)

        if request.method == 'POST':
            form = opacaoForm(request.POST) 
            if form.is_valid():
                opcao = form.save(commit=False)
                opcao.enquete = enquete
                opcao.save()
                return redirect('Enquete')
            else:
                return redirect('Enquete')
        data['form'] = form
        data['Opcao'] = enquete
        return render(request, 'usuarios/opcoes.html', data)   
