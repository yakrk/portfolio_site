from django.urls import path
from . import views  # viewsにあるすべてを持ってくる

urlpatterns = [
    path('', views.random_pokemon, name='random_pokemon'),
]
