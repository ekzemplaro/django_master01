from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		for user in User.objects.all():
			print(user.id,"\t", end="")
			print(user.username,"\t", end="")
			print(user.email)
