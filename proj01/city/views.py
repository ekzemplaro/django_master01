# ------------------------------------------------------------------
#
#	city/views.py
#
#						Feb/18/2019
#
# ------------------------------------------------------------------
import sys

from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from .models import City
from .forms import CityForm

# ------------------------------------------------------------------
def index(request):
	params = {
			'title': 'Cities',
			'message': 'All Cities.',
			'form': CityForm(),
			'data': [],
		}

	if(request.method == 'POST'):
		sys.stderr.write("*** views.py *** POST ***\n")
	else:
		sys.stderr.write("*** views.py *** else ***\n")
#
	params['data'] = City.objects.all()
#
	for unit in params['data']:
		print(unit.code,len(unit.towns),unit.towns[0])
#
	return render(request,'city/index.html',params)
#
# ------------------------------------------------------------------
def create(request):
	params = {
		'title': 'City',
		'form': CityForm(),
	}

	if(request.method == 'POST'):
		sys.stderr.write("*** create *** POST ***\n")
		obj = City()
		city = CityForm(request.POST, instance=obj)
		city.save()
		return redirect(to='/city')
	else:
		sys.stderr.write("*** create *** else ***\n")
#
	return render(request,'city/create.html',params)
#
# ------------------------------------------------------------------
def edit(request,code):
	sys.stderr.write("*** edit *** start ***\n")
	obj = City.objects.get(code=code)

	if(request.method == 'POST'):
		sys.stderr.write("*** edit *** POST ***\n")
		city = CityForm(request.POST, instance=obj)
		sys.stderr.write("*** edit *** bbbb ***\n")
		city.save()
		sys.stderr.write("*** edit *** cccc ***\n")
		return redirect(to='/city')
	else:
		sys.stderr.write("*** edit *** else ***\n")
#
	params = {
		'title': 'City',
		'code': code,
		'form': CityForm(instance=obj),
	}

	sys.stderr.write("*** edit *** end ***\n")

	return render(request,'city/edit.html',params)
#
# ------------------------------------------------------------------
def delete(request,code):
	sys.stderr.write("*** delete *** start ***\n")
	city = City.objects.get(code=code)
#
	if(request.method == 'POST'):
		sys.stderr.write("*** delete *** POST ***\n")
		city.delete()
		return redirect(to='/city')
	else:
		sys.stderr.write("*** delete *** else ***\n")
#
	params = {
		'title': 'City',
		'code': code,
		'obj': city,
	}

	sys.stderr.write("*** delete *** end ***\n")
	return render(request,'city/delete.html',params)
#
# ------------------------------------------------------------------
