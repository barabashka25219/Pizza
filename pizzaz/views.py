from django.shortcuts import render, redirect
from .models import Pizza
from .forms import PizzaForm

def index(request):
    return render(request, 'pizzaz/index.html')

def pizzaz_overview(request):
    pizzaz = Pizza.objects.order_by('-name')
    return render(request, 'pizzaz/pizzaz_overview.html', context={'pizzaz': pizzaz})

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-name')
    return render(request, 'pizzaz/pizza.html', context={'pizza': pizza, 'toppings': toppings})

def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzaz:pizzaz_overview')
    return render(request, 'pizzaz/new_pizza.html', context={'form': form})