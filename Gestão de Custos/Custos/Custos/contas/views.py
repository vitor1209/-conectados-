from django.shortcuts import render , redirect
from .models import Despesa
from django.urls import reverse

def home(request):
    return render(request, 'contas\home.html')

def novaDespesa(request):
    print('swswswsws')
    if request.method == 'POST':
        print('bgdbgdbf')
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        repeticao = request.POST.get('repeticao')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')


        if valor and float(valor) > 0:
            nova_despesa = Despesa(valor=valor, data=data, repeticao=repeticao, categoria=categoria, descricao=descricao)
            nova_despesa.save()
            return redirect('home')
        else:
            return render(request, 'contas/home.html', {'error': 'O valor deve ser preenchido e maior que zero.'})

    else:
        return render(request, 'home')  
