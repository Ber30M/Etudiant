from xml.dom import NoModificationAllowedErr
from django.db import models

# Create your models here.
genre = [
("M","Masculin"),
("F","Féminin")]

class Etudiant(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=26)
    prenom = models.CharField(max_length=26)
    genre = models.CharField(choices=genre, max_length=10)
    date_naissance = models.DateField()
    fac = models.CharField(max_length = 40)
    
class Cours(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=15)
    ponderation = models.IntegerField()
    Etudiant = models.ForeignKey("Etudiant", on_delete= models.CASCADE)

class Point(models.Model):
    id = models.AutoField(primary_key=True)
    point = models.FloatField()
    cours = models.ForeignKey("Cours", null = True, on_delete= models.SET_NULL)
    Etudiant = models.ForeignKey("Etudiant", on_delete=models.CASCADE)
    
    
    
    
    
    
    
    