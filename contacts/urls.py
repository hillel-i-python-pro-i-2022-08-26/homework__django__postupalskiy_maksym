from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.get_contact, name="index"),
    path("add-contact/", views.add_contact, name="add_contact"),
    path("search-contact/", views.search_contact, name="contact_search"),
    path("view-contact/", views.show_contact_search, name="contact_info"),
    path("delete-contact/<int:pk>/", views.delete_contact, name="contact_delete"),
    path("contact/contact-update/<int:pk>/", views.update_contact, name="contact_update"),
    path("contact/<int:pk>/", views.show_contact_info, name="contact"),
]
