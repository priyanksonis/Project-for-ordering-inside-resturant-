from django.db import models



class KitchenOrderBook(models.Model):
    order_id        = models.IntegerField()
    order_number    = models.IntegerField()                                                  #this will e same as id field in order table
    chefname        = models.CharField(max_length=120)
    time            = models.CharField(max_length=50)
    #time            = models.IntegerField(max_length=120)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.chefname

    @property
    def title(self):
        return self.chefname


