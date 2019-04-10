from django.conf.urls import url, include
from oscar import app

class MyShop(app.Shop):
    # Override get_urls method
    def get_urls(self):
        urls = [
            url(r'^catalog/',self.catalogue_app.urls),
            # all the remaining URLs, removed for simplicity
            # ...
        ]
        urls = urls + super(MyShop,self).get_urls()
        return urls


application = MyShop()