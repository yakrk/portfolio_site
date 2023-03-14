from django.urls import path
from . import views  # viewsにあるすべてを持ってくる


urlpatterns = [
    path('', views.blogs_top, name='blogs_top'),
    path("<int:post_id>/", views.post, name="post"),
]
