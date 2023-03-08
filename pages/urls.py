from django.urls import path
from . import views #viewsにあるすべてを持ってくる

#  listings

urlpatterns = [
    path('', views.index, name='index'),
]

