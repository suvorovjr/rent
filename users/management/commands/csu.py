from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='Admin',
            last_name='Admin'
        )
        user.set_password('admin')
        user.save()
