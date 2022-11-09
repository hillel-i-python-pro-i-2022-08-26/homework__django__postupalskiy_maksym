import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def session_info(request: WSGIRequest | HttpRequest) -> HttpResponse:
    session = request.session
    if not session.session_key:
        session.save()
    visit_time = session.get("visit_time", datetime.datetime.now())
    visits_count = session.get("count", 0)
    visits_count += 1
    session["count"] = visits_count
    return render(
        request,
        "session/index.html",
        {
            "title": "Session info",
            "session_id": session.session_key,
            "visits_count": visits_count,
            "visit_time": visit_time,
        },
    )
