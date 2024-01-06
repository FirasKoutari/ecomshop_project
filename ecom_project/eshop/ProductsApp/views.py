from django.shortcuts import render
from ProductsApp.models import ProductConfiguration,ProductItem,ProductCategory,Variation,VariationOption,Product,Promotion,PromotionCategory
from django.shortcuts import render, get_object_or_404
from django.views import View

# Create your views here.
def detail(request):
    return render(request,'detail.html')


def shop(request):
    prod = Product.objects.all()
    return render(request,'shop.html', {'prod': prod})


class ProductDetailView(View):
    template_name = 'detail.html'
    model = Product
    context_object_name = 'product'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, self.template_name, context)
