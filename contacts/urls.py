from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.ContactListView.as_view(), name="index"),
    path("add-contact/", views.ContactCreateView.as_view(), name="add_contact"),
    path("search-contact/", views.search_contact, name="contact_search"),
    path("view-contact/", views.show_contact_search, name="contact_info"),
    path("delete-contact/<int:pk>/", views.ContactDeleteView.as_view(), name="contact_delete"),
    path("contact/contact-update/<int:pk>/", views.ContactUpdateView.as_view(), name="contact_update"),
    path("contact/<int:pk>/", views.ContactView.as_view(), name="contact"),
]
