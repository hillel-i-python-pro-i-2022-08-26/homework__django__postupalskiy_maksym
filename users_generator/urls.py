from django.urls import path

from . import views

app_name = "users_generator"

urlpatterns = [
    path("", views.info_generator, name="index"),
    path("<int:number>", views.info_generator, name="index"),
]
