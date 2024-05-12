from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime  import datetime
from .models import Formation
from .forms import FormationForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'index.html',{})

def publications(request):
    return render(request, 'Publications.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def formations(request):
    liste_formations = Formation.objects.all()
    return render(request, 'Formations.html',{ 'liste_formations': liste_formations })

def ajouterformation(request):
    submitted = False
    if request.method == "POST":
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajouterformation?submitted=True')
    else:
        form = FormationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'AjouterFormations.html',{ 'form': form, 'submitted':submitted })