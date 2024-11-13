from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    return render(request, "pizzas/index.html")

def available(request):
    content = Pizza.objects.order_by("name")
    all_pizza = {"figure": content}
    return render(request, "pizzas/available.html", all_pizza)

def apart(request, pizza_id):
    content = Pizza.objects.get(id=pizza_id)
    ingr = content.topping_set.order_by("name")
    info = {"piz_name": content, "figure": ingr}
    return render(request, "pizzas/apart.html", info)