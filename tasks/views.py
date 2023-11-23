from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

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
                return HttpResponse('Usuario creado')
            except:
                return HttpResponse('El usuario ya existe')
        return HttpResponse('No coinciden las contraseñas')