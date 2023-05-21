#Voici les urls ou les chemin de l'application poste

from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',HomePage,name='homepage'),
    path('piergyDeveloppement/principale',Principale.as_view(),name='principale'),
    path('piergyDeveloppement/details/<str:pk>',Details, name='detail'),
    path('piergyDeveloppement/apropospage/',AproposPage,name='apropospage'),
    path('piergyDeveloppement/servicespage/',ServicesPage,name='servicespage'),
    path('piergyDeveloppement/ajoutArticle/', Ajout,name='ajoutArticle'),
    path('piergyDeveloppement/supprimerArticle/<str:pk>', Supprimer,name='supprimerArticle'),
    path('piergyDeveloppement/modif/<int:id>/', Modif, name='modif'),
    path('piergyDeveloppement/piergyDeveloppement/recherche/', Recherche, name='search'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 