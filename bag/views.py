from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Allow users add a quantity of a specific products to there bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    degrees = None

    if 'club_degrees' in request.POST:
        degrees = request.POST['club_degrees']
    bag = request.session.get('bag', {})

    if degrees:
        if item_id in list(bag.keys()):
            if degrees in bag[item_id]['clubs_by_degrees'].keys():
                bag[item_id]['clubs_by_degrees'][degrees] += quantity
                messages.success(request, f'Updated {product.name} {degrees.upper()} quantity to {bag[item_id]["clubs_by_degrees"][degrees]}')
            else:
                bag[item_id]['clubs_by_degrees'][degrees] = quantity
                messages.success(request, f'Added {product.name} {degrees.upper()} to your bag')
        else:
            bag[item_id] = {'clubs_by_degrees': {degrees: quantity}}
            messages.success(request, f'Added {product.name} {degrees.upper()} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Allow users update the quantity of a specific products to there bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    degrees = None

    if 'club_degrees' in request.POST:
        degrees = request.POST['club_degrees']
    bag = request.session.get('bag', {})

    if degrees:
        if quantity > 0:
            bag[item_id]['clubs_by_degrees'][degrees] = quantity
            messages.success(request, f'Updated {product.name} {degrees.upper()} quantity to {bag[item_id]["clubs_by_degrees"][degrees]}')
        else:
            del bag[item_id]['clubs_by_degrees'][degrees]
            if not bag[item_id]['clubs_by_degrees']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} {degrees.upper()} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Allow users to delete products from there bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        degrees = None

        if 'club_degrees' in request.POST:
            degrees = request.POST['club_degrees']
        bag = request.session.get('bag', {})

        if degrees:
            del bag[item_id]['clubs_by_degrees'][degrees]
            if not bag[item_id]['clubs_by_degrees']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} {degrees.upper()} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
