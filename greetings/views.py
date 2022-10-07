from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from apps.faker.apps import faker_name


def greetings(request: HttpRequest, name: str | None = None):
    if name is None:
        name = faker_name()
    return render(
        request,
        "greetings/index.html",
        {
            "title": "Greetings",
            "name": name.title(),
        },
    )