from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct
class Product(AbstractProduct):
    active = models.BooleanField(default=False)
from oscar.apps.catalogue.models import *
