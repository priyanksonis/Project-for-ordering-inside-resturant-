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
    	item[an_order]= Line.objects.filter(order_id=13)


    #list of items in a order
    #import pdb
    #pdb.set_trace()

    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)
