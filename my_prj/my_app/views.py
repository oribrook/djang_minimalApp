from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.views import View

from .models import Car


def home(request):
    return render(request=request, template_name='my_app/base.html')


def car_list(request):    
    
    

    sort_ = request.GET.get("sort", False)
    if sort_:        
        cars = Car.objects.only('car_type', 'cost', 'id').order_by(sort_)
    else:
        cars = Car.objects.only('car_type', 'cost', 'id')

    return render(request=request, template_name="my_app/cars_list.html",
                  context={'cars': cars})

def car(request, id):
    car = get_object_or_404(Car, id=id)   

    return render(request=request, template_name="my_app/car.html",
                context={'car': car})
