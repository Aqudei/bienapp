from django.core.management.base import BaseCommand, CommandError
from ._plotter import plot


class Command(BaseCommand):

    def handle(self, *args, **options):
        plot()