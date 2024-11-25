from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    path('', views.index, name='index'),
    path('available/', views.available, name='available'),
    path('available/<int:pizza_id>', views.apart, name="apart")
]