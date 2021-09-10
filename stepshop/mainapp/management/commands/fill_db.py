import os
import json

from mainapp.models import ProductCategory, Product
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

JSON_PATH = 'mainapp/fixtures'

def load_from_json(file_name):
    with open(file_name, mode='r', encoding='windows-1251') as f_obj:
        return json.load(f_obj)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json(os.path.join(JSON_PATH, 'categories.json'))

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = category.get('fields')
            new_category['id'] = category.get('pk')
            base_cat = ProductCategory(**new_category)
            base_cat.save()

        products = load_from_json(os.path.join(JSON_PATH, 'categories.json'))

        Product.objects.all().delete()

        for product in products:
            new_product = product.get('fields')
            category = product.get('category')
            _category = ProductCategory.objects.get(id=category)
            new_product['category'] = _category
            base_cat = Product(**new_product)
            base_cat.save()
