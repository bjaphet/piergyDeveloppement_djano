from django.db import models
from django.db import models
# Création de modeles

#Modele zero : les category des postes

class Category(models.Model):
    nom = models.CharField(max_length=250)

#Premier modele : les articles

class Article(models.Model):
    titre=models.CharField(max_length=25)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField(max_length=250)
    num=models.IntegerField(default=1)
    image=models.ImageField(null=True, blank=True, upload_to='media/')
    date_creation=models.DateTimeField(auto_now_add=True)#Pour voir la date et l'heure automatique
    date_mis_Ajour=models.DateTimeField(auto_now=True)
    
    #Pour afficher les plus recent
    class Meta:
        ordering=['-date_creation']

#Deuxieme modele : les commentaires

class Commentaire(models.Model):
    contenu=models.ForeignKey(Article, related_name='commentaires' , on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, default='Pas de nom')
    email = models.EmailField(max_length=254)
    corps = models.TextField()
    date_creation=models.DateTimeField(auto_now_add=True)#Pour voir la date et l'heure automatique
    date_mis_Ajour=models.DateTimeField(auto_now=True)
    
     #Pour afficher les plus recent
    class Meta:
        ordering=['-date_creation']

#Troisieme modele : Les insertion des do