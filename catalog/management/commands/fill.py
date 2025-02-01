from django.core.management import BaseCommand
from django.conf import settings
import os
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'fixtures/catalog.json')) as file:
            records = json.load(file)

        Category.objects.all().delete()
        Product.objects.all().delete()

        categories = []
        products = []

        for record in records:
            if record['model'] == 'catalog.category':
                fields = record['fields']
                categories.append(Category.objects.create(**fields))
            if record['model'] == 'catalog.product':
                fields = record['fields']
                fields['category'] = None
                products.append(Product.objects.create(**fields))
