# ------------------------------------------------------------------
#
#	models.py
#
#					Feb/23/2019
# ------------------------------------------------------------------
from django.db import models
from django_mysql.models import ListCharField

class City(models.Model):
	code = models.CharField(max_length=10,primary_key=True)
	name = models.CharField(max_length=20)
	population = models.IntegerField(default=0)
	towns = ListCharField(
        	models.CharField(max_length=10),size=6, max_length=(6 * 11))
	date_mod = models.DateField()

	def __str__(self):
		return '<City: ' + \
			self.code + ', ' + self.name + '>'
# ------------------------------------------------------------------
