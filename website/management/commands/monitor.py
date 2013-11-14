from django.core.management.base import BaseCommand, CommandError
from website.models import *

class Command(BaseCommand):
    help = 'Launch a monitoring batch'

    def handle(self, *args, **options):
        for check in Check.objects.all():
            check.check()
