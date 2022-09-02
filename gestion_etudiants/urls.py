from django.urls import path

from gestion_etudiants.views import hello_world
from . view import *

urlpatterns = [
    path('Bonjour/<str:nom>', hello_world),
]
