from django.views.generic import ListView
from products.models import Product

class Home(ListView):
    model = Product
    context_object_name='products'
    template_name = 'products/home.html'