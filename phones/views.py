from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    else:
        phones = Phone.objects.all().order_by('-price')

    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=slug).first()
    context = {
        'phone': phone_objects
    }
    return render(request, template, context)

