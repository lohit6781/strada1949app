from django.shortcuts import render, redirect, HttpResponse
from strada1949.models import Collection, Product, Order
from django.shortcuts import render
from django.template import RequestContext
import uuid
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from paywix.payu import Payu

# payu_config = settings.PAYU_CONFIG
# merchant_key = payu_config.get('merchant_key')
# merchant_salt = payu_config.get('merchant_salt')
# surl = payu_config.get('success_url')
# furl = payu_config.get('failure_url')
# mode = payu_config.get('mode')
# payu = Payu(merchant_key, merchant_salt, surl, furl, mode)

# Create your views here.
def home(request):
    collections = Collection.objects.all()
    products = Product.objects.filter(featured=True)

    context = {
        'collections' : collections,
        'products' : products,
    }
    return render(request, 'home.html', context)

def products(request, category):
    collections = Collection.objects.all()

    if category == 'men':
        products = Product.objects.filter(male=True)
        category_var = 'Men\'s'
    elif category == 'women':
        products = Product.objects.filter(female=True)
        category_var = 'Women\'s'
    elif category == 'overcoats-jackets':
        products = Product.objects.filter(female=True)
        category_var = 'Overcoats & Jackets'
    elif category == 'accessories':
        products = Product.objects.filter(female=True)
        category_var = 'Accessories'

    context = {
        'collections' : collections,
        'products' : products,
        'category_var' : category_var,
    }
    return render(request, 'products.html', context)

def collections(request, collection_url):
    collection_url = collection_url[slice(4)]
    collections = Collection.objects.all()
    products = Product.objects.all()

    category_var = 'from ' + str(collection_url)

    product_list = []

    for product in products:
        if str(product.collection) == str(collection_url):
            product_list.append(str(product.product_id))
        else:
            pass

    products = Product.objects.filter(product_id__in=product_list)

    context = {
        'collections' : collections,
        'products' : products,
        'category_var' : category_var,
    }
    return render(request, 'products.html', context)

def productView(request, product_id):

    if request.method == 'GET':

        product_id = product_id
        collections = Collection.objects.all()
        products = Product.objects.filter(product_id=product_id)

        context = {
            'collections' : collections,
            'products' : products,
        }
        return render(request, 'productView.html', context)

    elif request.method == 'POST':

        product_id = product_id
        collections = Collection.objects.all()
        products = Product.objects.filter(product_id=product_id)

        product = request.POST.get('product')
        size = request.POST.get('size')
        cart = request.session.get('cart')

        added_to_cart = True

        if cart:
            cart[product] = size
        else:
            cart = {}
            cart[product] = size

        request.session['cart'] = cart

        print('\n', request.session['cart'], '\n')

        context = {
            'cart' : str(request.session['cart']),
            'collections' : collections,
            'products' : products,
            'added_to_cart' : added_to_cart,
        }
        return render(request, 'productView.html', context)

def cart(request):

    if request.method == 'GET':

        cart = request.session.get('cart')
        collections = Collection.objects.all()

        if cart:
            items = cart.items()

            item_keys = []
            item_values = []

            for key, value in items:
                item_keys.append(key)
                item_values.append(value)

            products = Product.objects.filter(product_id__in=item_keys)

            total = 0

            for product in products:
                total += int(product.price)

            checkout = True

            context = {
                'items' : items,
                'products' : products,
                'checkout' : checkout,
                'total' : total,
                'collections' : collections,
            }

            return render(request, 'cart.html', context)

        else:
            checkout = False

            context = {
                'checkout' : checkout,
                'collections' : collections,
            }

            return render(request, 'cart.html', context)

    if request.method == 'POST':

        deleted_item = request.POST.get('deleted_item')

        if request.session['cart'][str(deleted_item)]:
            del request.session['cart'][str(deleted_item)]
        else:
            redirect('Cart')

        request.session.modified = True
        
        cart = request.session.get('cart')
        collections = Collection.objects.all()

        if cart:
            items = cart.items()

            item_keys = []
            item_values = []

            for key, value in items:
                item_keys.append(key)
                item_values.append(value)

            products = Product.objects.filter(product_id__in=item_keys)

            total = 0

            for product in products:
                total += int(product.price)

            checkout = True

            context = {
                'items' : items,
                'products' : products,
                'checkout' : checkout,
                'total' : total,
                'collections' : collections,
            }

            return render(request, 'cart.html', context)

        else:
            checkout = False

            context = {
                'checkout' : checkout,
                'collections' : collections,
            }

            return render(request, 'cart.html', context)

def redirection(request):
    request.session['cart']
    cartVal = request.session['cart']

    product_list = []
    product_sizes = []

    for i in cartVal:
        product_list.append(i)
        product_sizes.append(cartVal[i])

    order_list = Product.objects.filter(product_id__in=product_list)

    fin_order_list = []

    for j in range(len(product_list)):
        fin_order = str(order_list[j]) + ' - ' + str(product_sizes[j])
        fin_order_list.append(fin_order)

    billing = {
        'first_name' : request.POST.get('first_name'),
        'last_name' : request.POST.get('last_name'),
        'address1' : request.POST.get('address1'),
        'address2' : request.POST.get('address2'),
        'city' : request.POST.get('city'),
        'state' : request.POST.get('state'),
        'zip_code' : request.POST.get('zip_code'),
        'email' : request.POST.get('email'),
        'phone' : request.POST.get('phone'),
        'order' : fin_order_list,
        'totalVal' : request.POST.get('totalVal')
    }

    request.session['billing'] = billing

    # Order.objects.create(
    #     first_name = request.POST.get('first_name'),
    #     last_name = request.POST.get('last_name'),
    #     address1 = request.POST.get('address1'),
    #     address2 = request.POST.get('address2'),
    #     city = request.POST.get('city'),
    #     state = request.POST.get('state'),
    #     zip_code = request.POST.get('zip_code'),
    #     email = request.POST.get('email'),
    #     phone = request.POST.get('phone'),
    #     order = fin_order_list
    # )

    # del request.session['cart']

    return redirect(test)

def termsConditions(request):
    return render(request, 'termsConditions.html')

def test(request):
    try:
        request.session['billing']

        amount = request.session['billing']['totalVal']
        first_name = request.session['billing']['first_name']
        email = request.session['billing']['email']
        phone = request.session['billing']['phone']
        order = request.session['billing']['order']
        last_name = request.session['billing']['last_name']
        address1 = request.session['billing']['address1']
        address2 = request.session['billing']['address2']
        city = request.session['billing']['city']
        state = request.session['billing']['state']
        zip_code = request.session['billing']['zip_code']

        data = {
            'amount': str(amount),
            'firstname': str(first_name),
            'email': str(email),
            'phone': str(phone),
            'productinfo': str(order),
            'lastname': str(last_name),
            'address1': str(address1),
            'address2': str(address2),
            'city': str(city), 
            'state': str(state),
            'country': 'India',
            'zipcode': str(zip_code),
            'udf1': '',
            'udf2': '',
            'udf3': '',
            'udf4': '',
            'udf5': '',
            'txnid': uuid.uuid4
        }
        
        return render(request, 'payu_checkout.html', {'posted': data})

        context = {
            'val' : request.session['billing']
        }
    
    except:
        context = {
            'val' : 'zeroVal'
        }

    return render(request, 'test.html', context)

def success(request):
    return HttpResponse('Success')

def failure(request):
    return HttpResponse('Failure')

def handler404(request, *args, **argv):
    response = render('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

def deleteSession(request):
    del request.session['cart']
    del request.session['billing']
    return redirect(home)