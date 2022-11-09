from django.contrib import admin
from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list = ("name", "phone", "b_day", "is_auto_generated")
    search_fields = ("name", "phone")
    list_filter = ("is_auto_generated",)
    date = "b_day"
    ordering = ("-modified_at", "-created_at")
    help_text = "Name, Phone or Name"
