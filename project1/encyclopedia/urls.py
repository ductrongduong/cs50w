from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name = "newpage"),
    path("editpage/<str:title>", views.editpage, name = "editpage"),
    path("random", views.random_page, name = "random"),
    path("<str:name>", views.entry, name = "entry")
]
