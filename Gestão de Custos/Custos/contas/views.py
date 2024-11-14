from django.shortcuts import render , redirect
from .models import Despesa
from django.views.generic import ListView

def home(request):
    return render(request, 'contas\home.html')

def novaDespesa(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        repeticao = request.POST.get('repeticao')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')

        nova_despesa = Despesa(valor=valor, data=data, repeticao=repeticao, categoria=categoria, descricao=descricao)
        nova_despesa.save()
        return redirect('home')

    else:
        return render(request, 'home')  

class DespesasListView(ListView):
    model = Despesa
    template_name = "contas/filtroDespesas.html"
    context_object_name = 'despesa'
    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.GET.get('filtroCategoria')
        
        if categoria:
           queryset = queryset.filter(categoria=categoria)
        return queryset
