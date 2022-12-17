from django.core.management import BaseCommand, CommandParser
import logging
from middlewares import models


class Command(BaseCommand):
    help = "Delete session info"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "-ds",
            "--delete_sessions",
            help="Delete session info",
            action="store_true",
        )

    def handle(self, *args, **options):
        amount_of_session_info = models.VisitorsRequests.objects.all().count()
        self.logger.info(f"Amount session: {amount_of_session_info}")

        if options["delete_sessions"]:
            all_info = models.VisitorsRequests.objects.all()
            all_info.delete()

        deleting_number = models.VisitorsRequests.objects.all().count()
        deleted_session_info = amount_of_session_info - deleting_number

        self.logger.info(f"Delete session info: {deleted_session_info}")

        deleting_number = models.VisitorsRequests.objects.all().count()
        self.logger.info(f"Amount users: {deleting_number}")
