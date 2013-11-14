from django.core.management.base import BaseCommand, CommandError
from website.models import *
import time

class Command(BaseCommand):
    help = 'Launch a monitoring process'

    def handle(self, *args, **options):
        while True:
            for metric in Metric.objects.all():
                metric.check()
            time.sleep(1)
