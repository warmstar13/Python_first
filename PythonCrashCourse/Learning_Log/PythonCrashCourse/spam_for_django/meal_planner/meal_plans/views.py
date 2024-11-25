from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'meal_plan/start.html')