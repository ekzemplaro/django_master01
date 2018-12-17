# ------------------------------------------------------------------
#
#	create_users.py
#
#					Dec/17/2018
# ------------------------------------------------------------------
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

users = ['user01','user02','user03','user04','user05']
class Command(BaseCommand):
	help = 'Create users'

	def handle(self, *args, **kwargs):
		for user in users:
			email = user + "@test.com"
			password = 'saluton123'
			User.objects.create_user(username=user, email=email, password=password)
#
# ------------------------------------------------------------------
