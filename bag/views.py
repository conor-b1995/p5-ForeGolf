from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Allow users add a quantity of a specific products to there bag """

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
            else:
                bag[item_id]['clubs_by_degrees'][degrees] = quantity
        else:
            bag[item_id] = {'clubs_by_degrees': {degrees: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)
