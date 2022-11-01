from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from webargs import fields
from webargs.djangoparser import use_args

from apps.services.generate_user_info import sort_info


@use_args({"amount": fields.Int(missing=10)}, location="query")
def info_generator(request: HttpRequest, args) -> HttpResponse:
    amount = args["amount"]
    return render(
        request,
        "users_generator/index.html",
        {
            "title": "Users",
            "info": sort_info(amount=amount),
        },
    )
