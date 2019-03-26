"""frobshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



#from django.conf.urls import include, url  # < Django-2.0
from django.urls import include, path  # > Django-2.0
from django.contrib import admin
#from oscar.app import application

from django.conf import settings
from django.conf.urls.static import static


#from .app import application
from frobshop.app import application as shop
from django.conf.urls import url, include


from yourappsfolder.kitchen import views



urlpatterns = [
    #url(r'^i18n/', include('django.conf.urls.i18n')),
    path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    #url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),  # > Django-2.0

    #url(r'', application.urls),
    #path('', application.urls),  # > Django-2.0
    url(r'', shop.urls),

    url(r'^orders_in_kitchen/$', views.KitchenBook.as_view()),
    #path(r'^orders_in_kitchen_new/$', views.KitchenBook.as_view(), name='kitchen_book'),
    #url(r'^orders_in_kitchen_new/$', views.KitchenBook.as_view()),
    #url(r'^orders_in_kitchen_new/$', views.Index.as_view()),
    #url(r'^orders_in_kitchen_new1/$', views.KitchenBook1.as_view()),

    #url(r'^orders_in_kitchen_new_final/$', views.KitchenBook2.as_view()),

    #url(r'^orders_in_kitchen/$', views.Index.as_view(), name='index'),

    #path(r'^orders_in_kitchen/$', views.Index.as_view(), name='index'),

    #path('orders_in_kitchen/', include('yourappsfolder.kitchen.urls')),

    #path('admin_1/', admin.site.urls),
    #path('accounts/', include('yourappsfolder.accounts.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('1/', include('yourappsfolder.kitchen.urls')),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# from django.conf.urls import include, url
# from frobshop.app import application
# urlpatterns = [
#    # Your other URLs
#    url(r'', include(application.urls)),
# ]


