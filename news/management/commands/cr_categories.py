from django.core.management import BaseCommand
from news.models import Categories


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories_list = ['Путешествия', 'Путеводитель', 'Достопримечательности']
        for categories in categories_list:
            new_category = Categories.objects.create(name=categories)
            new_category.save()
