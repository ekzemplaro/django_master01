# ------------------------------------------------------------------
#
#	management/commands/show_cities.py
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
		instance = City.objects.all()
		for city in instance:
			str_out = city.code + "\t"
			str_out += city.name + "\t"
			str_out += str(city.population) + "\t"
			str_out += str(city.date_mod) + "\t"
			print(str_out)
#
		print("---")
#
		for unit_aa in instance.values():
			str_out = unit_aa['code'] + "\t"
			str_out += unit_aa['name'] + "\t"
			str_out += str(unit_aa['population']) + "\t"
			str_out += str(unit_aa['date_mod']) + "\t"
			print(str_out)
#
# ------------------------------------------------------------------
