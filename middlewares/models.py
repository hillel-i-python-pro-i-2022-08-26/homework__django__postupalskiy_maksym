from django.conf import settings
from django.db import models


class VisitorsRequests(models.Model):
    session_key = models.CharField(max_length=255)
    path = models.SlugField(max_length=255)
    visits_count = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    last_visit_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Visit Info"
