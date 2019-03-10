#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

#from .models import RestaurantLocation


from oscar.apps.order.models import Order
from oscar.apps.order.models import Line


def orders_listview(request):
    template_name = 'kitchen/orders.html'
    queryset = Order.objects.all()

    queryset_items=Line.objects.filter(order_id=13)


    item={}

    for an_order in queryset:
    	item[an_order.id]= Line.objects.filter(order_id=an_order.id)

    

    #list of items in a order
    #import pdb
    #pdb.set_trace()


    for i in item:
    	print(i)

    context = {
        "object_list": queryset,
        "items_in_orders":item,
    }
    #import pdb
    #pdb.set_trace()
    return render(request, template_name, context)