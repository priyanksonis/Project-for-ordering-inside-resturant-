from oscar.apps.checkout.views import ShippingAddressView as CoreShippingAddressView
from oscar.apps.checkout.views import ShippingMethodView as CoreShippingMethodView
from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView


class ShippingAddressView(CoreShippingAddressView):
	print('hi')
	#template_name='checkout/payment_details.html'

class ShippingMethodView(CoreShippingMethodView):
	template_name='checkout/payment_details.html'


class PaymentDetailsView(CorePaymentDetailsView):
	template_name='checkout/preview.html'


