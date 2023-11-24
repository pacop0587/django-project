from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signup(request):
    """Funcion signup"""
    contexto = {'form':UserCreationForm}
    print(request.method)
    if request.method == 'GET':
        return render(request, 'signup.html',contexto)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
            except:
                contextError = {'error': 'Usuario repetido','form':UserCreationForm}
                return render(request, 'signup.html', contextError)
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
            })