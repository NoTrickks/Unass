from django.contrib import admin
from .models import Formation
from .models import Formateur
from .models import Superviseur
from .models import Client

# Register your models here.
admin.site.register(Formation)
admin.site.register(Formateur)
admin.site.register(Superviseur)
admin.site.register(Client)