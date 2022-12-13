from django.views.generic import TemplateView, ListView
from middlewares.models import VisitorsRequests
from middlewares.services.aggregations import aggregator


class MiddlewaresView(TemplateView):
    template_name = "middlewares/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Middleware"
        return context


class AllRequestInfoView(ListView):
    model = VisitorsRequests
    template_name = "middlewares/all_sessions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "All Sessions"
        session_request = VisitorsRequests.objects.all()
        context['object_list'] = session_request
        context.update(aggregator(session_request))
        return context


class CurrentRequestInfoView(ListView):
    model = VisitorsRequests
    template_name = "middlewares/current_session.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current session info"
        session_request = VisitorsRequests.objects.filter(session_key=self.kwargs['session_key'])
        context['object_list'] = session_request
        context.update(aggregator(session_request))
        return context


class CurrentUserInfoView(ListView):
    model = VisitorsRequests
    template_name = "middlewares/current_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current user info"
        session_request = VisitorsRequests.objects.filter(user=self.kwargs['pk'])
        context['object_list'] = session_request
        context.update(aggregator(session_request))
        return context

