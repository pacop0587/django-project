from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    """Funcion signup"""
    contexto = {'form':UserCreationForm}
    return render(request, 'signup.html',contexto)