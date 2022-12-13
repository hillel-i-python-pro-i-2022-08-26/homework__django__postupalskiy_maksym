from django.db.models import QuerySet, Sum, Count
from middlewares.services.types_structures import RequestData


def aggregator(queryset: QuerySet) -> RequestData:
    total_visits = queryset.aggregate(Sum("count_of_visits")).get("count_of_visits__sum")
    total_pages = queryset.aggregate(Count("path")).get("path__count")
    return {"total_visits": total_visits, "visited_pages": total_pages}
