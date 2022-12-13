from django.urls import path

from middlewares import views

app_name = "middlewares"

urlpatterns = [
    path("", views.MiddlewaresView.as_view(), name="index"),
    path("info/", views.AllRequestInfoView.as_view(), name="all_info"),
    path("session/<slug:session_key>/", views.CurrentRequestInfoView.as_view(), name="session_info"),
    path("user/<int:pk>/", views.CurrentUserInfoView.as_view(), name="user_info"),
]
