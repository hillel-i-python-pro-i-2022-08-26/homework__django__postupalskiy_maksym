from django.urls import path

from session import views


app_name = "session"

urlpatterns = [path("", views.session_info, name="session")]
