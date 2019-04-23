from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct
class Product(AbstractProduct):
    active = models.BooleanField(default=False)
    active_new=models.BooleanField(default=True)
from oscar.apps.catalogue.models import *




class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
