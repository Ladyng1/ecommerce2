from django.shortcuts import render
from .models import Product

# Create your views here.


def home(request):
    products = Product.object.all()

    context = {"products": products}
    return render(request, "core/index,html", context)




