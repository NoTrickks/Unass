from django.db import models

# Create your models here.



class Formateur(models.Model):
    NomFormateur = models.CharField('Nom du formateur', max_length=120)
    PrenomFormateur = models.CharField('Prénom du formateur', max_length=120)
    AdresseMail = models.EmailField('Adresse mail', max_length=120)
    NumeroTelephone = models.CharField('Numéro de téléphone', max_length=120)

    def __str__(self):
        return self.NomFormateur + ' ' + self.PrenomFormateur


class Superviseur(models.Model):
    NomSuperviseur = models.CharField('Nom du superviseur', max_length=120)
    PrenomSuperviseur = models.CharField('Prénom du superviseur', max_length=120)    
    AdresseMail = models.EmailField('Adresse mail', max_length=120)
    NumeroTelephone = models.CharField('Numéro de téléphone', max_length=120)

    def __str__(self):
        return self.NomSuperviseur + ' ' + self.PrenomSuperviseur



class Client(models.Model):
    NomClient = models.CharField('Nom', max_length=120)
    PrenomClient = models.CharField('Prénom', max_length=120)
    Entreprise = models.CharField('Entreprise', max_length=120)    
    AdresseMail = models.EmailField('Adresse mail', max_length=120)
    NumeroTelephone = models.CharField('Numéro de téléphone', max_length=120) 

    def __str__(self):
        return self.NomClient + ' ' + self.PrenomClient


class Formation(models.Model):    
    NomFormation = models.CharField('Nom de la formation', max_length=120)
    DescriptionFormation = models.CharField('Description', max_length=120)
    DateFormation = models.DateTimeField('Date de la formation', max_length=120)
    NomClient = models.CharField('Nom du client', max_length=120)
    LieuFormation = models.CharField('Lieu de la formation', max_length=120)
    ResponsableFormation = models.CharField('Responsable de la formation', max_length=120)
    Formateurs = models.ManyToManyField(Formateur, blank=True)
    Participants = models.ManyToManyField(Client, blank=True)
    EtatValidation = models.BooleanField('Etat de validation', default=False, blank=True)
    #Foreign = models.FiregnKey(Class,..)
    def __str__(self):
        return self.NomFormation
