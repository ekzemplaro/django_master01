from django import forms
from .models import City

class CityForm(forms.ModelForm):
	class Meta:
		model = City
		fields = ['code','name','population','towns','date_mod']
#
