"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#from restaurents.views import home, about, contact ,ContactView ,ContactTemplateView

from django.views.generic import TemplateView
#from restaurents.views import restaurant_listview

from django.contrib.auth.views import LoginView

from restaurents.views import (
    restaurant_listview,
    RestaurantListView,
    RestaurantDetailView,
    restaurant_createview,
    RestaurantCreateView

)



# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     #url(r'^$', home),
#     #url(r'^about/$', about),
#     #url(r'^contact/$', contact),
#     #url(r'^contact/$', ContactView.as_view()),   #url for class basec view

#     #use this when we want  to give  some argument (kwargs)  ex.:: http://127.0.0.1:8000/contact/2/    instead of http://127.0.0.1:8000/contact/
#     #url(r'^contact/(?P<id>\d+)/$', ContactView.as_view()),   #url for class basec view
#     #url(r'^contact/$', ContactTemplateView.as_view()), #for template based views


   

#     url(r'^$', HomeView.as_view()),  #because we have extra context in Homeview
#     url(r'^about/$', TemplateView.as_view(template_name='about.html')),
#     url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),





#]



# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', TemplateView.as_view(template_name='home.html')),
#     url(r'^restaurants/$', restaurant_listview),
#     url(r'^about/$', TemplateView.as_view(template_name='about.html')),
#     url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
# ]
    


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', TemplateView.as_view(template_name='home.html')),
#     url(r'^restaurants/$', RestaurantListView.as_view()),
#     url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
#     #url(r'^restaurants/asian/$', AsianFusionRestaurantListView.as_view()),
#     url(r'^about/$', TemplateView.as_view(template_name='about.html')),
#     url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
# ]




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^restaurants/$', RestaurantListView.as_view()),
    url(r'^restaurants/create/$', RestaurantCreateView.as_view()),
    #url(r'^restaurants/create/$',   restaurant_createview ), # RestaurantCreateView.as_view()),
    #url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    #url(r'^restaurants/asian/$', AsianFusionRestaurantListView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
]