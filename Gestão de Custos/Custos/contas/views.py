from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Despesa
from django.views.generic import ListView
import json


def home(request):
    context = {
        'usuario': request.user.username
    }
    return render(request, 'contas\home.html',context)

def novaDespesa(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        repeticao = request.POST.get('repeticao')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')

        nova_despesa = Despesa(valor=valor, data=data, repeticao=repeticao, categoria=categoria, descricao=descricao, usuario=request.user)
        nova_despesa.save()
        return redirect('home')

    else:
        return render(request, 'home')  

class DespesasListView(ListView):
    model = Despesa
    template_name = "contas/filtroDespesas.html"
    context_object_name = 'despesa'
    def get_queryset(self):
        queryset = Despesa.objects.filter(usuario=self.request.user)
        queryset = super().get_queryset()
        categoria = self.request.GET.get('filtroCategoria')
        
        if categoria:
           queryset = queryset.filter(categoria=categoria)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todas_despesas'] = Despesa.objects.filter(usuario=self.request.user)

        return context


def metas(request):

    labels = []
    data = []   
    percentual = []

    queryset = Despesa.objects.filter(usuario=request.user).order_by('-valor')

    for conta in queryset:
        if conta.categoria in labels:
            indice = labels.index(conta.categoria)
            dataValor = data[indice]
            data[indice] = dataValor + conta.valor
        else :
            labels.append(conta.categoria)
            data.append(conta.valor)

    total = sum(data)
    for n in data:
        n = (n / total) * 100
        percentual.append(round(n))


    combined_data = zip(labels, data , percentual)
    
    data = [float(d) for d in data]  
    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
        'combined_data': combined_data,
        'percentual' : percentual
    }
    return render(request, 'contas\metas.html', context)  