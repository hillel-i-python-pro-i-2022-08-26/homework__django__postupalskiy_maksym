from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.UserSingUpView.as_view(), name="signup"),
    path("edit/<int:pk>/", views.UserUpdateView.as_view(), name="edit"),
]
