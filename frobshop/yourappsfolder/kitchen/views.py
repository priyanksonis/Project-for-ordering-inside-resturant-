#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView ,CreateView ,ListView ,UpdateView ,DetailView
from django.views.generic.edit import BaseCreateView,  TemplateResponseMixin
from django.views.generic.list import BaseListView

#from .models import RestaurantLocation



from .forms import KitchenBookForm
from .models import KitchenOrderBook

#rom oscar.apps.order.models import Order
from ..order.models import Order
from oscar.apps.order.models import Line
from ..address.models import UserAddress



class KitchenBook(CreateView):
    """docstring for ClassName"""
    #queryset = Order.objects.all()

    order_obj = Order.objects.all()
    template_name = 'kitchen/orders.html'
    
    
    success_url="/orders_in_kitchen/"
    form_class = KitchenBookForm
    ####
    print("priyank")
    def get_context_data(self, **kwargs):
        order_obj = Order.objects.all()
        item={}
        row_in_KitchenOrderBook_table={}

        f_name_dict={}
        user_id={}

        for an_order in order_obj:
            item[an_order.id]= Line.objects.filter(order_id=an_order.id)
            row_in_KitchenOrderBook_table[an_order.id]=KitchenOrderBook.objects.filter(order_id = an_order.id)
            user_id_val=Order.objects.filter(id=an_order.id).values_list('user_id')[0][0]
            #f_name_=UserAddress.objects.filter(user_id=user_id_val).values_list('first_name')[0][0]



            #import pdb
            #pdb.set_trace()

        context = super(KitchenBook, self).get_context_data(**kwargs)
        context["object_list"] = order_obj
        context["items_in_orders"] = item
        context["kitchen_orders_book"] = row_in_KitchenOrderBook_table
        context["f_name_of_orderer"]=f_name_dict

        #import pdb
        #pdb.set_trace()
        return context


