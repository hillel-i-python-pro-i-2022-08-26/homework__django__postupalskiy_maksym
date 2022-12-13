import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def session_info(request: WSGIRequest | HttpRequest) -> HttpResponse:
    session = request.session
    if not session.session_key:
        session.save()
    visit_time = session.get("visit_time", datetime.datetime.now())
    count_of_visits = session.get("count", 0)
    count_of_visits += 1
    session["count"] = count_of_visits
    return render(
        request,
        "session/index.html",
        {
            "title": "Session info",
            "session_id": session.session_key,
            "count_of_visits": count_of_visits,
            "visit_time": visit_time,
        },
    )
