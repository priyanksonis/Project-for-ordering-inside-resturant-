from oscar.apps.catalogue.views import CatalogueView as CoreCatalogueView

from oscar.apps.catalogue.views import ProductDetailView as CoreProductDetailView


from django.shortcuts import render
from .models import Video
from .forms import VideoForm


class CatalogueView(CoreCatalogueView):
	print("hi")


class ProductDetailView(CoreProductDetailView):
	print("hi")
		


def showvideo(request):

    lastvideo= Video.objects.last()

    videofile= lastvideo.videofile


    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'videofile': videofile,
              'form': form
              }
    
      
    return render(request, 'detail.html', context)

