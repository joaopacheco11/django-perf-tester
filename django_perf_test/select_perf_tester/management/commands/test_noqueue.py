from django.core.management.base import BaseCommand
from select_perf_tester.models import TestModel1, Queue
class Command(BaseCommand):
    def handle(self, **options):
        print(TestModel1.objects.all().filter(index_field=2).order_by('ifield2')[:1].explain(verbose=True))