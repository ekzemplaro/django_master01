# ------------------------------------------------------------------
#
#	management/commands/population_copy.py
#
#						Feb/18/2019
#
# ------------------------------------------------------------------
from django.core.management.base import BaseCommand
from city.models import City

# ------------------------------------------------------------------
class Command(BaseCommand):
	help = 'Display cities'

	def handle(self, *args, **kwargs):
		city_a = City.objects.get(code ='t3328')
		vx = city_a.population
		city_b = City.objects.get(code ='t3329')
		setattr(city_b,'population',vx)
		city_b.save()
#
# ------------------------------------------------------------------
