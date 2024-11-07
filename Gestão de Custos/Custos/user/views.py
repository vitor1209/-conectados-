from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html', {
            'form': UserCreationForm(),
        })
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()

                login(request, user)
                return redirect('sigin')
            else:
                return render(request, 'user/signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Suas senhas são diferentes.'
                })
        
        except User.DoesNotExist:
            return render(request, 'user/signup.html', {
                'form': UserCreationForm(),
                'error': 'Usuário já existe.'
            })
        
def sigin(request):

    if request.method == 'GET':
        return render(request, 'user/sigin.html', {
            'form': AuthenticationForm(),
        })
    
    else:
        user = authenticate( request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            print('vdvf')
            return render(request , 'user/sigin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuário ou senha está incorreto.'
            })

        else:
            print('aeaeaeae')
            login(request, user)
            return redirect('signup') 