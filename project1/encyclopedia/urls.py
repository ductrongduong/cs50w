from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name = "newpage"),
    path("<str:name>", views.entry, name = "entry")
]
