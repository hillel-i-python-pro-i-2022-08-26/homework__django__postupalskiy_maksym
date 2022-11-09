from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from contacts.models import Contact
from contacts.forms import AddContactForm
from django.contrib import messages


def get_contact(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()
    return render(
        request, "contacts/index.html", {"title": "Contact", "contacts": contacts}
    )


def add_contact(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        form = AddContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            messages.success(request, "Contact added successfully")
            return redirect("contacts:contact", pk=contact.pk)
    else:
        form = AddContactForm(request.POST)
    return render(
        request,
        "contacts/add_contact.html",
        {
            "title": "Add Contact",
            "form": form,
        },
    )


def search_contact(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "contacts/search_contact.html",
        {
            "title": "Search Contact",
        },
    )


def show_contact_search(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q")
    if query.startswith("0"):
        contact = Contact.objects.get(phone=query)
    else:
        contact = Contact.objects.get(pk=query)
    return render(
        request,
        "contacts/show_contact_search.html",
        {
            "title": f"Show Contact {contact.name}",
        },
    )


def delete_contact(request: HttpRequest, pk: Contact.pk) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    messages.success(request, f"Contact {contact.name} deleted")
    return redirect("contacts:index")


def update_contact(request: HttpRequest, pk: Contact.pk) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = AddContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated")
            return redirect("contacts:contact", pk=pk)
        else:
            form = AddContactForm(instance=contact)
        return render(
            request,
            "contacts/update_contact.html",
            {
                "title": "Contact Update",
                "form": form,
            },
        )


def show_contact_info(request: HttpRequest, pk: Contact.pk) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=pk)
    return render(
        request,
        "contacts/show_contact_info.html",
        {
            "title": f"info {contact.name}",
            "contact": contact,
        },
    )
