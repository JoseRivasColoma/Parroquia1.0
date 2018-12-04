from django.shortcuts import render, redirect, render_to_response
from .models import Comunidad, TipoPersona, TipoEvento, Persona
from django.contrib import messages

def VariableBase(request):
    tipos_persona = TipoPersona.objects.all()
    variables = {
        'tp':tipos_persona
    }

    return variables
