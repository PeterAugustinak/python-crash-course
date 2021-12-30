from django.shortcuts import render

from .models import Pizza


# Create your views here.
def index(request):
    """The home page for Pizza app."""
    return render(request, 'pizza/index.html')


def pizzas(request):
    """The 'Pizzas' page of Pizzeria shows all pizzas."""
    pizzas = Pizza.objects.order_by('pizza_name')
    context = {'pizzas': pizzas}
    return render(request, 'pizza/pizzas.html', context)


def pizza(request, pizza_id):
    """Shows a single pizza and all its toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('topping_name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizza/pizza.html', context)
