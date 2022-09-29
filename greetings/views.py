from django.http import HttpResponse, HttpRequest
from apps.faker.apps import faker_name


def greetings(request: HttpRequest, name=faker_name()):
    return HttpResponse(f"Hi, {name.title()}, welcome to the greetings page!")
