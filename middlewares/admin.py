from django.contrib import admin
from . import models


@admin.register(models.VisitorsRequests)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("session_key", "path", "user", "count_of_visits")
    search_fields = ("user", "session_key", "path")
    list_filter = ("user",)
    list_per_page = 20
