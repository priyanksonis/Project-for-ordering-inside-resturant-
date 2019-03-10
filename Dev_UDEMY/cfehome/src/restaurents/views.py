import random
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from django.views import View   #imported because we are using class based view
from django.views.generic import TemplateView ,ListView ,DetailView ,CreateView#for template based views
from django.db.models import Q

from django.shortcuts import render, get_object_or_404
# # Create your views here.

# #creating a function based vieww
# def home_old(request):

# 	html_var='f string'
# 	html_= """<!doctype html>
#     <html lang="en">
#     <head>
#     </head>

#     <body>

#     <h1>Hello world</h1>
#     <p>This is {html_var} through</p>

#     </body>
#     </html>
#     """ 
#     #f string   is used in python 3 for string substitution

# 	#render takes 3 args (request, template, context(a dictionary))
# 	#return HttpResponse("hello")
	
# 	return HttpResponse(html_)

# 	#return render(request,"base.html",{"html_var":True})

# def home(request):
# 	num=None
# 	some_list=[random.randint(0,100000),random.randint(0,100000),random.randint(0,100000)]	

# 	conditional_bool_item=True

# 	if conditional_bool_item:
# 		num=random.randint(0,100000)
# 	context={"bool_item":True,
# 	"num":num,
# 	"some_list":some_list
# 	}
# 	return render(request,"home.html",context)

# def about(request):
# 	context={}
# 	return render(request,"about.html",context)

# def contact(request):
# 	context={}
# 	return render(request,"contact.html",context)		


# #class based view

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context={}
#         print(kwargs)
#         return render(request, "contact.html", context)


# class ContactTemplateView(TemplateView):
# 	template_name="contact.html"
        	        




# class HomeView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         num = None
#         some_list = [
#             random.randint(0, 100000000), 
#             random.randint(0, 100000000), 
#             random.randint(0, 100000000)
#         ]
#         condition_bool_item = True
#         if condition_bool_item:
#             num = random.randint(0, 100000000)
#         context = {
#             "num": num, 
#             "some_list": some_list
#         }
#         return context


from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

from .models import RestaurantLocation







# def restaurant_createview(request):
#     # if request.method == "GET":
#     #     print("get data")
#     if request.method == "POST":
#         title = request.POST.get("title") #request.POST["title"]
#         location = request.POST.get("location")
#         category = request.POST.get("category")
#         obj = RestaurantLocation.objects.create(
#                 name = title,
#                 location= location,
#                 category = category

#             )
#         return HttpResponseRedirect("/restaurants/")
#     template_name = 'restaurents/form.html'
#     context = {}
#     return render(request, template_name, context)



def restaurant_createview(request):
    form = RestaurantCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        obj = RestaurantLocation.objects.create(
                name = form.cleaned_data.get('name'),
                location= form.cleaned_data.get('location'),
                category = form.cleaned_data.get('category')

            )
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors = form.errors
           
    template_name = 'restaurents/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)








def restaurant_listview(request):
    template_name = 'restaurents/restaurents_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)



class RestaurantListView(ListView):
	template_name = 'restaurents/restaurents_list.html'
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
                    Q(category__iexact=slug) |
                    Q(category__icontains=slug)
                )
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset


class RestaurantDetailView(DetailView):
	#template_name = 'restaurents/restaurantlocation_detail.html'
	queryset = RestaurantLocation.objects.all()
	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id
	# 	return obj






class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurents/form.html'
    success_url = "/restaurants/"