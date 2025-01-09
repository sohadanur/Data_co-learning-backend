# import json
# from django.core.management.base import BaseCommand
# #from .models import *
# #from . import load_data  # Assuming load_data.py is in the parent directory
# from data.models import *
# from . import load_data  # Import from the current directory

# class Command(BaseCommand):
#     help = 'Load data from JSON files into the database'

#     def load_data_from_json(filename, model_class):
#         with open(filename) as f:
#             data = json.load(f)
#             for item in data:
#                 model_class.objects.create(**item)
            
import json
from django.core.management.base import BaseCommand
from data.models import Country, State, City

class Command(BaseCommand):
    help = 'Load data from JSON files into the database'

    def handle(self, *args, **kwargs):
        # Load Country data
        with open(r'C:\Users\ADMIN\Desktop\Bacbon\codes\co-learning-backend\data\management\commands\country.json') as f:
            countries = json.load(f)
            for country in countries:
                Country.objects.get_or_create(id=country["id"], defaults=country)

        # Load State data
        with open(r'C:\Users\ADMIN\Desktop\Bacbon\codes\co-learning-backend\data\management\commands\state.json') as f:
            states = json.load(f)
            for state in states:
                try:
                    country = Country.objects.get(id=state["country_id"])
                    State.objects.get_or_create(id=state["id"], defaults={"name": state["name"], "country": country})
                except Country.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Country with id {state['country_id']} does not exist"))

        # Load City data
        with open(r'C:\Users\ADMIN\Desktop\Bacbon\codes\co-learning-backend\data\management\commands\city.json') as f:
            cities = json.load(f)
            for city in cities:
                try:
                    state = State.objects.get(id=city["state_id"])
                    City.objects.get_or_create(id=city["id"], defaults={"name": city["name"], "state": state})
                except State.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"State with id {city['state_id']} does not exist"))

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

