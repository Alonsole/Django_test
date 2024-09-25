import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, required=False, help='Path to CSV file.')

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_model = Phone()
            phone_model.name = phone['name'] if len(phone['name']) > 0 else "None Phone"
            phone_model.price = float(phone['price'])
            phone_model.image = phone['image']
            phone_model.release_date = phone['release_date']
            phone_model.lte_exists = bool(phone['lte_exists'])
            phone_model.slug = slugify(phone_model.name)
            if not Phone.objects.filter(slug=phone_model.slug).exists():
                phone_model.save()
            else:
                print(f"Телефон: '{phone_model.name}' уже есть в базе, повторная загрузка невозможна")


