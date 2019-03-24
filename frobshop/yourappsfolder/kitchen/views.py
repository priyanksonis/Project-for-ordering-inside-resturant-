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

from oscar.apps.order.models import Order
from oscar.apps.order.models import Line


def orders_listview(request):
    template_name = 'kitchen/orders.html'
    queryset = Order.objects.all()

    queryset_items=Line.objects.filter(order_id=13)
    item={}
    row_in_KitchenOrderBook_table={}

    form = KitchenBookForm(request.POST, request.FILES)

    for an_order in queryset:
        item[an_order.id]= Line.objects.filter(order_id=an_order.id)
        row_in_KitchenOrderBook_table[an_order.id]=KitchenOrderBook.objects.filter(order_id = an_order.id)
    context = {"object_list": queryset,
     "items_in_orders":item,
     "kitchen_orders_book":row_in_KitchenOrderBook_table,
     }
    return render(request, template_name, context)


def orders_listview1(request,template_name = 'kitchen/orders.html'):
    if request.method == 'POST':
        form = KitchenBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # This will save the user.
            # Add the user's role in the User Role table below?
        #


        queryset = Order.objects.all()

        queryset_items=Line.objects.filter(order_id=13)
        item={}
        row_in_KitchenOrderBook_table={}

        form = KitchenBookForm(request.POST, request.FILES)


        for an_order in queryset:
            item[an_order.id]= Line.objects.filter(order_id=an_order.id)
            row_in_KitchenOrderBook_table[an_order.id]=KitchenOrderBook.objects.filter(order_id = an_order.id)
        context = {"object_list": queryset,
        "items_in_orders":item,
        "kitchen_orders_book":row_in_KitchenOrderBook_table,
        }
         
        request.method == 'GET'
    else:

        # The form should be passed through. This will be processed when the form is submitted on client side via this functions "if request.method == 'POST'" branch.
        form = KitchenBookForm()

        queryset = Order.objects.all()

        queryset_items=Line.objects.filter(order_id=13)
        item={}
        row_in_KitchenOrderBook_table={}

        form = KitchenBookForm(request.POST, request.FILES)

        for an_order in queryset:
            item[an_order.id]= Line.objects.filter(order_id=an_order.id)
            row_in_KitchenOrderBook_table[an_order.id]=KitchenOrderBook.objects.filter(order_id = an_order.id)
        context = {"object_list": queryset,
        "items_in_orders":item,
        "kitchen_orders_book":row_in_KitchenOrderBook_table,
        }
        request.method == 'POST'
     #"form": form}
    #import pdb
    #pdb.set_trace()
    return render(request, template_name, context)





class KitchenBook(CreateView):
    """docstring for ClassName"""
    
    template_name = 'kitchen/orders_new.html'
    queryset = Order.objects.all()
    item={}
    row_in_KitchenOrderBook_table={}
    for an_order in queryset:
        item[an_order.id]= Line.objects.filter(order_id=an_order.id)
        row_in_KitchenOrderBook_table[an_order.id]=KitchenOrderBook.objects.filter(order_id = an_order.id)

    
    success_url="/orders_in_kitchen_new/"
    form_class = KitchenBookForm

    def get_context_data(self, **kwargs):
        context = super(KitchenBook, self).get_context_data(**kwargs)
        context["object_list"] = self.queryset
        context["items_in_orders"] = self.item
        context["kitchen_orders_book"] = self.row_in_KitchenOrderBook_table
        return context














class UploadFileView(CreateView):
    form_class = KitchenBookForm
    success_url = "/orders_in_kitchen_new/"
    template_name = 'kitchen/orders_new.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = KitchenOrderBook.objects.all()
        return super(UploadFileView, self).get_context_data(**kwargs)








class FormAndListView(BaseCreateView, BaseListView, TemplateResponseMixin):
    def get(self, request, *args, **kwargs):
        formView = BaseCreateView.get(self, request, *args, **kwargs)
        listView = BaseListView.get(self, request, *args, **kwargs)
        formData = formView.context_data['form']
        listData = listView.context_data['object_list']
        return render_to_response('textfrompdf/index.html', {'form' : formData, 'all_PDF' : listData},
                           context_instance=RequestContext(request))






from django.views.generic.list import MultipleObjectMixin, MultipleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView

class ListAppendView(MultipleObjectMixin,
        MultipleObjectTemplateResponseMixin,
        ModelFormMixin,
        ProcessFormView):
    """ A View that displays a list of objects and a form to create a new object.
    The View processes this form. """
    template_name_suffix = 'orders_new1'
    template_name_suffix = template_name_suffix[-30:]
    allow_empty = True
    form_class = KitchenBookForm


    def get(self, request, *args, **kwargs):
        #self.object_list = self.get_queryset()
        self.object_list = KitchenOrderBook.objects.all()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object_list=self.object_list, form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = None
        return super(ListAppendView, self).post(request, *args, **kwargs)

    def form_invalid(self, form):
        #self.object_list = self.get_queryset()
        self.object_list = KitchenOrderBook.objects.all()
        return self.render_to_response(self.get_context_data(object_list=self.object_list, form=form))






# class Index(ListView):
#     model = KitchenOrderBook
#     context_object_name = 'books'
#     template_name = 'kitchen/orders.html'
#     #template_name = 'index.html'
#     qs=KitchenOrderBook.objects.all()



#     queryset = Order.objects.all()

#     queryset_items=Line.objects.filter(order_id=13)
#     item={}
#     row_in_KitchenOrderBook_table={}

#     #form = KitchenBookForm(request.POST, request.FILES)

#     for an_order in queryset:
#         item[an_order.id]= Line.objects.filter(order_id=an_order.id)
#         row_in_KitchenOrderBook_table[an_order.id]=KitchenOrderBook.objects.filter(order_id = an_order.id)
#     # context = {"object_list": queryset,
#     #  "items_in_orders":item,
#     #  "kitchen_orders_book":row_in_KitchenOrderBook_table,
#     #  }
    



#     def get_context_data(self, **kwargs):
#             context = super(Index,self).get_context_data(**kwargs)
#             #context['now'] = timezone.now()
#             context["object_list"] = self.queryset
#             context["items_in_orders"] = self.item
#             context["kitchen_orders_book"] = self.row_in_KitchenOrderBook_table
#             return context






# # Django
# from django.contrib.messages.views import SuccessMessageMixin
# from django.urls import reverse_lazy
# from django.views import generic
# # Project
# from .forms import BookForm
# from .models import Book
# from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin


# class Index(generic.ListView):
#     model = Book



#     #import pdb
#     #pdb.set_trace()

#     context_object_name = 'books'
#     template_name = 'index.html'


#     queryset = Order.objects.all()

#     queryset_items=Line.objects.filter(order_id=13)


#     item={}

#     for an_order in queryset:
#         item[an_order.id]= Line.objects.filter(order_id=an_order.id)

    

#     #list of items in a order
#     #import pdb
#     #pdb.set_trace()


#     #for i in item:
#         #print(i)

#     queryset1=Book.objects.all()    

#     context = {
#         "object_list": queryset,
#         "items_in_orders":item,
#         'books':queryset1,
#     }
    

#     def get(self, request, *args, **kwargs):
#         context=self.context
#         #context = {}
#         return render(request, "index.html", context)








# # class Index(generic.ListView):
# #     model = Book
# #     context_object_name = 'books'
# #     template_name = 'index.html'





# # Create
# class BookCreateView(PassRequestMixin, SuccessMessageMixin,
#                      generic.CreateView):
#     template_name = 'kitchen/create_book.html'
#     form_class = BookForm
#     success_message = 'Success: Book was created.'
#     success_url = reverse_lazy('index')


# # Update
# class BookUpdateView(PassRequestMixin, SuccessMessageMixin,
#                      generic.UpdateView):
#     model = Book
#     template_name = 'kitchen/update_book.html'
#     form_class = BookForm
#     success_message = 'Success: Book was updated.'
#     success_url = reverse_lazy('index')


# # Read
# class BookReadView(generic.DetailView):
#     model = Book
#     template_name = 'kitchen/read_book.html'


# # Delete
# class BookDeleteView(DeleteAjaxMixin, generic.DeleteView):
#     model = Book
#     template_name = 'kitchen/delete_book.html'
#     success_message = 'Success: Book was deleted.'
#     success_url = reverse_lazy('index')
