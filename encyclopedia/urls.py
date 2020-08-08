from django.urls import path

from . import views

urlpatterns = [
    path("wiki/<str:title>", views.title, name="title"),
    path("wiki/search/", views.search, name='search'),
    path("wiki/", views.index, name="index")
]
