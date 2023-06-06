from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.views import View
from .models import Car
from django.db.transaction import atomic
from .forms import ContactForm


def serve_contact(request):
    if request.method == 'GET':
        return render(request=request, template_name='my_app/contact.html',
                    context={'form': ContactForm(initial={'car_type': 'Suzuki'})})


def search_car(request):
    if request.method == 'GET':
        return render(request=request, 
                      template_name="my_app/search_car.html")

    if request.method == 'POST':
        query = Car.objects.only('car_type', 'cost', 'id')        
        
        if len(request.POST.get("car_type")) > 0:
            query = query.filter(car_type__contains=request.POST.get("car_type"))
        if len(request.POST.get("max_cost")) > 0:
            query = query.filter(cost__lte=float(request.POST.get("max_cost")))
        if len(request.POST.get("min_cost")) > 0:
            query = query.filter(cost__gte=float(request.POST.get("min_cost")))
        
        return render(request=request, template_name="my_app/cars_list.html",
                  context={'cars': list(query)})


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
