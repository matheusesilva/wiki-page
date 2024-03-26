from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.wiki, name="entry"),
    path("new", views.createNew, name="new"),
    path("random", views.randomPage, name="random"),
    path("wiki/<str:title>/edit", views.editPage, name="edit")
]
