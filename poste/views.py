from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article,Category
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
# from .form import ArticleForm
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.conf import settings


#Class qui donne la page d'acceuil elle herite du module ListView de django
class Principale(ListView):
    #Affichage du template équivaut à return render(request,'home.html) 
    template_name='principale.html'
    #Permet de recuperer tout les fichers et les afficher
    queryset= Article.objects.all()
    #Présisions du nombre de page ou d'élement sur le templates ici que 4 élements
    paginate_by=2

def HomePage(request):
    return render(request,'home.html')
     
def AproposPage(request):
    #Ce qui veut dire : prends tout les objects qui se trouve dans la classe Article donne là à la variable list_Article
    list_Article=Article.objects.all()
    #Ce qui veut dire : prends les valeurs recu dans la variable list_Article envoie là à liste_Article qui le renvoie à son tour au context
    context={'liste_Article':list_Article}
    #Ce qui veut dire : Apres avoir pris les valeurs donc le context affiche les avec la page web 
    return render (request, 'apropos.html', context)

def ServicesPage(request):
      return render(request,'service.html')


#Fonction pour voir les details d'un aticle en particulier
@login_required(login_url='connection')
def Details(request,pk):
    articles = Article.objects.get(id=pk)
    #Obtention de la categories
    category = articles.category
    #Obternir la liste des élements de même categorie "Donc ce de 
    #la même categories vont etre recupererer et affecter à la variable article_en_relation"
    articles_en_relation = Article.objects.filter(category=category)[:3]#Pour préciser le nombres de postes à affiche /Tableau python
    context = {'article':articles,'articlesEnRelation':articles_en_relation}
    return render(request, 'details.html',context)
        
#Fonction pour l'ajout des données dans la BD
@login_required(login_url='connection')
def Ajout(request):
    if request.method == 'POST': 
        titre = request.POST['titre']
        desc = request.POST['desc']
        num = request.POST['num']
        image = request.FILES['image']
        
        #Récupération des categorie dans la table en fonction de la clé primaire
        categorie = Category.objects.get(pk=request.POST['categorie'])
        newPost = Article(titre=titre,desc=desc,num=num,image=image,category=categorie)
        newPost.save()
        return redirect('principale')
    else:
        #Récupération de toutes les  categorie dans la table pour l'affichage 
        categories = Category.objects.all()
        return render(request, 'ajout-donnees.html',{"categories":categories})


@login_required(login_url='connection')
def Modif(request, id):
    article = get_object_or_404(Article, id=id )
    if request.method == "POST":
        titre = request.POST['titre']
        num = request.POST['num']
        #Récupération des categorie dans la table en fonction de la clé primaire
        categorie = Category.objects.get(pk=request.POST['categorie'])
        desc = request.POST['desc']
        image = request.FILES.get('image')
        article.num=num
        article.categorie=categorie
        article.desc=desc
        if image:
            #Vérification de l'image
            if not image.content_type.startswitch('image'):
                return HttpResponse ("Le fichier entré n'est pas une image ")
            fs =  FileSystemStorage()
            fs.save(image.name, image)
            article.image = fs.url(image.name)
            # article.image=image
        article.save()
        return redirect('principale')
    else:
        categories = Category.objects.all()
        context = {'article':article,"categories":categories}
    return render (request, 'modifier-donnees.html',context)

#Suppression des donnees
@login_required(login_url='connection')
def Supprimer(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        article. delete()
        return redirect('principale')
    context ={'item':article}
    return render(request, 'supprimer-donnees.html',context) 

#Recherche des données
def Recherche(request):
    #récuperation des données en fonction de article qui est le name qui se trouve dans header html 
    query = request.GET.get('article')
    list_article = Article.objects.filter(titre__icontains=query)
    liste_article = Article.objects.filter(desc__icontains=query)
    contexte ={"list_article":list_article,"liste_article":liste_article }
    return render(request, 'recherche.html',contexte )