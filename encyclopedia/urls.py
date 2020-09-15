from django.urls import path

from . import views

urlpatterns = [

    path("wiki/search/", views.search, name='search'),
    path("wiki/create/", views.create, name="new"),
     path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("wiki/random/", views.ran, name="ran"),
    path("wiki/<str:title>", views.title, name="title"),
    path("wiki/", views.index, name="index")


]
