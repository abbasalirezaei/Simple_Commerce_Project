from django.views.generic import ListView
from products.models import Product
from .filters import ProductFilter  
class Home(ListView):
    model = Product
    context_object_name='products'
    template_name = 'products/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context