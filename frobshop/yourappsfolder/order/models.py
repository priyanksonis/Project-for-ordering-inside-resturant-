#from oscar.apps.order.models import *  # noqa isort:skip


#from oscar.apps.order.models import Order

from django.db.models.signals import post_save


from django.contrib.auth.models import User

from ..kitchen.signal import * 











def rec_function(sender,**kwargs):
	#import pdb
	#pdb.set_trace()
	print("Order receieved")


#when Order model is save a signal is sent to signal_from_order_model function of kitchen.signal
#post_save.connect(signal_from_order_model,sender=Order)





from django.db import models

from oscar.apps.order.abstract_models import AbstractOrder

class Order(AbstractOrder):
	print('hi')
#    first_name_as_user_table = models.CharField(max_length=120)
from oscar.apps.order.models import *



















