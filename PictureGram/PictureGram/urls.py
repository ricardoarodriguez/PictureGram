### PictureGram URLs module ###

from django.contrib import admin
from django.urls import path
from PictureGram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sorted_integers),
    path('signin_validation/<str:name>/<int:age>/', local_views.sign_in_validation),

    path('posts/', posts_views.list_post),
]
