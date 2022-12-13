from django.db.models import QuerySet, Sum, Count
from middlewares.services.types_structures import RequestData


def aggregator(queryset: QuerySet) -> RequestData:
    total_visits = queryset.aggregate(Sum('visits_count')).get('visits_count__sum')
    total_pages = queryset.aggregate(Count('path')).get('path__count')
    return {
        "total_visits": total_visits,
        "visited_pages": total_pages
    }