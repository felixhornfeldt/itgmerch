from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .models import Product

# Create your views here.
cart_url = 'cart'


def index(request):
    context = {
        'cart_url': cart_url
    }
    return render(request, 'main/index.html', context=context)


def product(request):
    if request.method == 'GET':
        product_id = request.GET.get('id', '999')
        actual_product = Product.objects.get(id_n=product_id)
        sizes = eval(actual_product.sizes)
        # print(product_id)
        # if int(product_id) == 1:
        #    return HttpResponse('Hey you made it!!!')

        context = {
            'product': actual_product,
            'cart_url': cart_url,
            'sizes': sizes,
        }

    return render(request, 'main/product.html', context=context)


def cart(request):
    if request.method == 'POST':
        # Ta in produkter som skall inhandlas
        # Skicka vidare till beställningssidan

        return HttpResponseRedirect('/order/')
    else:
        return render(request, 'main/cart.html')

# END OF CODE
