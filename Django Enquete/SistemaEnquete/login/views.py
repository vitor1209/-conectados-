from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def visualizacao(request):
    if request.method == "POST":
        form =  UserCreationForm(request.POST)
        print('vfvfvffvf')
        if form.is_valid():
            print('bjndgjbnbmpogb')
            form.save()
            return redirect('Enquete')
        else:
         print(form.errors)
    else:
        form = UserCreationForm()
        print('zazazazazaz')
    return render(request, 'registration/signup.html', {'form':form})