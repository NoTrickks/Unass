from django import forms                
from django.forms import ModelForm
from .models import Formation
import datetime

#Creation de la fiche pour la formation

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['NomFormation', 'DescriptionFormation', 'DateFormation', 'LieuFormation', 'NomClient', 'ResponsableFormation', 'Formateurs', 'Participants']
        widgets = {
            'NomFormation': forms.TextInput(attrs={'class':'form-control'}),
            'DescriptionFormation': forms.TextInput(attrs={'class':'form-control'}),
            'DateFormation': forms.DateInput(format='%d/%m/%Y',attrs={'class':'form-control'}),
            'LieuFormation': forms.TextInput(attrs={'class':'form-control'}),
            'NomClient': forms.TextInput(attrs={'class':'form-control'}),
            'ResponsableFormation': forms.TextInput(attrs={'class':'form-control'}),            
                   }
        


