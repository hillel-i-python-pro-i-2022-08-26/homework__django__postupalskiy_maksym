import logging

from django.core.management import BaseCommand, CommandParser

from contacts import models
from apps.services.contact_generator import return_contact


class Command(BaseCommand):
    help = "Generate required amount of contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "amount",
            type=int,
            metavar="NUMBER",
            default=10,
            help="generate amount of contacts(default 10)",
        )
        parser.add_argument(
            '-i', '--ignore',
            action='store_true',
            help='generate contacts with is_auto_generate=False',
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]
        self.logger.info(f"Generate {amount} of users info")
        number_of_generations = models.Contact.objects.all().count()
        self.logger.info(f"Now amount of users info is: {number_of_generations}")

        for count, info in enumerate(return_contact(amount=amount), start=1):
            self.logger.info(f"Generate: {count} of {amount}")
            if not options['ignore']:
                info.is_auto_generated = True
            if options['amount'] > 100:
                raise Exception("It's going to be hard to delete")
            info.save()
            self.logger.info(f"Generate {count} of {amount} DONE")

        info_after_generating = models.Contact.objects.all().count()
        self.logger.info(f"Amount of contacts after generating: {info_after_generating}")