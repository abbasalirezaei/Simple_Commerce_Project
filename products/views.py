from django.views.generic import ListView
from products.models import Product

class Home(ListView):
    model = Product
    template_name = 'products/home.html'