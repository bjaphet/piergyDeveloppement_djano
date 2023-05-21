
from django.urls import path
from .views import *

urlpatterns = [
    path('piergyDeveloppement/connection/',Connection,name='connection'),
    path('piergyDeveloppement/creation/',Creation,name='creation'),
    path('piergyDeveloppement/deconnection/',Deconnection,name='deconnection'),
    path('piergyDeveloppement/404Error/connection',PageError,name='404'),
]