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
        # Get_user_session__start
        session = request.session
        if not session.session_key:
            session.save()
        session_key = session.session_key
        # Get_user_session__stop

        logger_message = f"Path:{request.path} - User:{request.user} - Session:{session_key}"

        # Get_response__start
        self.logger.info(f"Before - {logger_message}")
        response: HttpResponse = self.get_response(request)
        self.logger.info(f"After - {logger_message}")
        # Get_response__stop

        visit_handler = VisitorsRequests.objects.filter(session_key=session_key, path=request.path).first()

        if visit_handler is not None:
            count_of_visits = visit_handler.count_of_visits
        else:
            visit_handler = VisitorsRequests()
            count_of_visits = 0
            if request.user.is_authenticated:
                visit_handler.user = request.user

            visit_handler.path = request.path
            visit_handler.session_key = session_key

        count_of_visits += 1
        session["count"] = count_of_visits
        visit_handler.count_of_visits = session["count"]

        visit_handler.save()

        return response
