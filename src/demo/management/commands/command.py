from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('user_name', type=str)

    def handle(self, *args, **options):
        username = options['user_name']
        self.stdout.write(self.style.SUCCESS('We called a custom command'))
