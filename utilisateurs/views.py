from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
# Création des fonctions pour les utilisateurs

#Creation de compte
def Creation(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                return render(request, 'connection.html', {'error': "Ce nom d'utilisateur exciste déjà ! réessayez ."})
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                messages.success(request, 'Compte crée avec succès connectez-vous maintenant')
                return redirect('connection')
        else:
            return render(request, 'connection.html', {'error': 'Les mots de passe ne sont pas identique ! rérssayez .'})
    else:
        return render(request, 'creation.html')
############################################################################################################################
    
# Connection ou login
def Connection(request):
    if request.method == 'POST':
        if 'login_attempts' in request.session:
            login_attempts = request.session['login_attempts']
            if login_attempts >= 3:
                messages.error(request, "Vous avez atteint la limite de tentatives de connexion. c'est la cause de cette rédirectrion réessayez plus tard")
                return redirect('404')
        # Traitement de la soumission du formulaire de connexion
        #Recupere les valeurs de la
        # class LoginForm
        form = LoginForm(request.POST)
        #Si les données saisi sont correctes
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username,password=pwd)
            #Si cela a marché redirige vers la page d'acceuil
            if user is not None:
                #Permet de stocker les infos de utlisateur connecte 
                login(request,user )
                messages.success(request,"Bravo!!! Bienvenue🤩🤗!")
                if 'login_attempts' in request.session:
                    del request.session['login_attempts']
                return redirect('principale')
            else:
                # Incrémentation du nombre de tentatives de connexion
                if 'login_attempts' in request.session:
                    request.session['login_attempts'] += 1
                else:
                    request.session['login_attempts'] = 1
                messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe invalide. Réessayez 😥")
    else:
        form = LoginForm()
    return render(request, 'connection.html', {'form': form})
            
           
###################################################################################################### #

#Deconnection

def Deconnection(request):
    logout(request)
    return redirect('homepage')


#Page d'erreur
# @login_required(login_url='connection')
def PageError(request):
    return render(request,'404.html')