from django.shortcuts import render
from .models import Pizza

def index(request):
    return render(request, 'pizzaz/index.html')

def pizzaz_overview(request):
    pizzaz = Pizza.objects.order_by('-name')
    return render(request, 'pizzaz/pizzaz_overview.html', context={'pizzaz': pizzaz})

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-name')
    return render(request, 'pizzaz/pizza.html', context={'pizza': pizza, 'toppings': toppings})
