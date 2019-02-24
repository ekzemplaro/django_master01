#!/usr/bin/env python
#
import os
import sys

from django.core.management.base import BaseCommand
from .models import City

instance = City.objects.all()
#
