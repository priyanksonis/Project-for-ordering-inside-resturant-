# Django
from django import forms
#from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


from .models import KitchenOrderBook

class KitchenBookForm(forms.ModelForm):

	class Meta:
	        model = KitchenOrderBook
	        fields = [
	        	'order_id',
	            'chefname',
	            'time',
	        ]
	        def clean_name(self):
	        	chefname = self.cleaned_data.get("chefname")
	        	if chefname == "Hello":
	        		raise forms.ValidationError("Not a valid name")
	        	return chefname
