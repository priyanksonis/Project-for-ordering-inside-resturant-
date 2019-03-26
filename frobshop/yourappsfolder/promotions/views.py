from oscar.apps.promotions.views import HomeView as CoreHomeView
from ..catalogue.views import CatalogueView as CoreCatalogueView


#from oscar.app.
from django.contrib.auth.models import User




#we are overriding  so that on home page we can show all the products
class HomeView(CoreCatalogueView):
	#template_name='catalogue/browse_new.html'

	print("hi")
	qs=User.objects.all()
	for i in qs:
		print(i.first_name)
	print(qs)
	x=2
	#import pdb
	#pdb.set_trace()