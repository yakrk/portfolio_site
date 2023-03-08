from django.urls import path
from . import views #viewsにあるすべてを持ってくる

urlpatterns = [
    path('', views.color_palette, name='color_palette'),
]

