from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct
class Product(AbstractProduct):
    active = models.BooleanField(default=False)
    active_new=models.BooleanField(default=True)
from oscar.apps.catalogue.models import *
