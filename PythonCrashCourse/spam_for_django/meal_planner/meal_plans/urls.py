from django.urls import path

from . import views

app_name = "meal_plans"
urlpatterns = [
    path('', views.start, name='start')
]