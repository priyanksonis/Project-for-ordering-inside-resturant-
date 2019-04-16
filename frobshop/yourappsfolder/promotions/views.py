from oscar.apps.promotions.views import HomeView as CoreHomeView
from ..catalogue.views import CatalogueView as CoreCatalogueView

from django.views.generic import TemplateView ,CreateView ,ListView ,UpdateView ,DetailView

#from oscar.app.
from django.contrib.auth.models import User
from ..order.models import Order
from ..kitchen.models import KitchenOrderBook
#chirag 14-04-19
from django.http import JsonResponse


#we are overriding  so that on home page we can show all the products
class HomeView(CoreCatalogueView,ListView):
    #template_name='catalogue/browse_new.html'
    print("hi")
    #qs=User.objects.all()
    #for i in qs:
    #    print(i.first_name)
    #print(qs)
    
    #def my_view(request):
    #i=0



    def get_context_data(self, **kwargs):
        try:
            i=0
            print(i)
            i=i+1
            username = None
            #import pdb
            #pdb.set_trace()
            self.object_list = self.get_queryset()
            user = User.objects.get(username=self.request.user.username)
            context = super(HomeView, self).get_context_data(**kwargs)
            context["val"]=i
            #context["object_list"]="object_list"
            #context["uname"]=user
            print(user.first_name)
            print(user.id)

            order_id_for_crnt_usr=Order.objects.filter(user_id=user.id)
            print(order_id_for_crnt_usr)
            
            #prints all orders ids for logged in usr 
            for ii in order_id_for_crnt_usr:
            	print(ii.id)
            
            #getting latest entry from KitchenOrderBook	
            KitchenOrderBookQS=KitchenOrderBook.objects.filter(order_id=50).last()
            
            #this holds <order_id, latest_object_of_KitchenOrderBook> for current user
            ord_id_KitchenOrderBook={}

            for ii in order_id_for_crnt_usr:
            	ord_id_KitchenOrderBook[ii.id]=KitchenOrderBook.objects.filter(order_id=ii.id).last()
            	#print(ii.id)
            

            context["ord_id_KitchenOrderBook"]=ord_id_KitchenOrderBook
            #import pdb
            #pdb.set_trace()
            return context
            #return JsonResponse(ord_id_KitchenOrderBook)
        except:
            pass    

    def get_queryset(self):
       """Return the last five published questions."""
       #qqs=User.objects.get(username=request.user.username)
       #print(qqs.first_name)
       #print("hello")
       #return qqs
    # def process_request(self, request):
    # 	user = User.objects.get(username=request.user.username)
    # 	print("hello")
    # 	print(user.first_name)

        #if request.user.is_authenticated:
            #username = request.user.username
            #print("u_name= %s", username)
    #     x=2
    # #import pdb
    # #pdb.set_trace()




class HomeView1(CoreCatalogueView,ListView):
    #template_name='catalogue/browse_new.html'
    print("hi")