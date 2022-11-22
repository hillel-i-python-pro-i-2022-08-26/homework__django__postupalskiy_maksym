from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView
from django.shortcuts import render
from contacts.models import Contact
from django.urls import reverse_lazy


class ContactListView(ListView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "phone",
        "b_day",
        "avatar",
    )

    def get_success_url(self):
        return reverse_lazy("contacts:contact", kwargs={"pk": self.object.pk})


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


@method_decorator(login_required, name="post")
class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:index")


@method_decorator(login_required, name="post")
class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "name",
        "phone",
        "b_day",
        "avatar",
    )
    template_name_suffix = "_update_form"

    def get_success_url(self):
        contact_pk = self.kwargs["pk"]
        return reverse_lazy("contacts:contact", kwargs={"pk": contact_pk})


class ContactView(TemplateView):
    template_name = "contacts/show_contact_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = Contact.objects.get(pk=context["pk"])
        context["contact"] = contact
        context["title"] = f"Info {contact.name}."
        return context
