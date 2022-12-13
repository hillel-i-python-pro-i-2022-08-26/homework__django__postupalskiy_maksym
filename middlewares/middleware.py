import logging
from typing import Callable
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from middlewares.models import VisitorsRequests


class LoggingMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info("Start")

    def __call__(self, request: WSGIRequest):
        session = request.session

        if not session.session_key:
            session.save()

        session_key = session.session_key

        log_message = f"Path:{request.path} - User:{request.user} - Session:{session_key}"

        self.logger.info(f"[before] {log_message}")
        response: HttpResponse = self.get_response(request)
        self.logger.info(f"[after] {log_message}")

        visit_request = VisitorsRequests.objects.filter(session_key=session_key, path=request.path).first()

        if visit_request is not None:
            count_visitors = visit_request.count_visitors
        else:
            visit_request = VisitorsRequests()
            count_visitors = 0
            if request.user.is_authenticated:
                visit_request = request.user

            visit_request.path = request.path
            visit_request.session_key = session_key

        count_visitors += 1
        session['count'] = count_visitors
        visit_request.count_visitors = session['count']

        visit_request.save()

        return response