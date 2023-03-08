from django.urls import path
from . import views #viewsにあるすべてを持ってくる
from django.views.decorators.csrf import csrf_exempt, csrf_protect

#  listings

urlpatterns = [
    path('', views.blogs_top, name='blogs_top'),
    path("<int:post_id>", views.post, name="post"),
]

