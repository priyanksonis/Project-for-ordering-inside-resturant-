from oscar.apps.promotions.views import HomeView as CoreHomeView
from ..catalogue.views import CatalogueView as CoreCatalogueView




#we are overriding  so that on home page we can show all the products
class HomeView(CoreCatalogueView):
	print("hi")
