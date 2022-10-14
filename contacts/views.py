from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from contacts.models import Contact


def get_contact(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {
        "title": 'Contact',
        "contacts": contacts
    })