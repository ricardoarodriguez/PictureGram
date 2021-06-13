### PictureGram URLs module ###

from django.contrib import admin
from django.urls import path
from PictureGram import views


urlpatterns = [
    path('hello-world/', views.hello_world),
    path('hi/', views.hi),
]
