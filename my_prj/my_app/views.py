from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.views import View
from .models import Car
from django.db.transaction import atomic
from .forms import ContactForm, CarForm
from django.conf import settings


@require_http_methods(["GET", "POST"])
def add_car(request):
    if request.method == 'GET':

        return render(request=request, template_name="my_app/form.html",
                    context={'form': CarForm, 
                             'head_message': 'הוספת מכונית',
                             'url': reverse('add_car')})

    # else (post):

    form = CarForm(request.POST)
    if not form.is_valid():
        return render(request=request, template_name="my_app/form.html",
                    context={'form': form, 
                             'head_message': 'הוספת מכונית - טפל בשגיאות',
                             'url': reverse('add_car')})
    else:
        form.save()
        return render(request=request, template_name='my_app/base.html',        
                    context= {'message': 'הטופס התקבל בהצלחה'})


class ContactView(View):    
    def get(self, request):
        return render(request=request, template_name='my_app/form.html',
                    context={'form': ContactForm(initial={'car_type': 'Suzuki'}),
                             'url': reverse('contact'),
                             'head_message': 'צור קשר'})
    
    def post(self, request):
        form = ContactForm(data=request.POST)        
        if not form.is_valid():
            return render(request=request, template_name='my_app/form.html',
                    context={'form': form,
                             'url': reverse('contact'),
                             'head_message': 'צור קשר - טפל בשגיאות'})

        # save file if exists
        if request.FILES.get('img', False):
            f = request.FILES['img']
            path = str(settings.BASE_DIR) + fr"\my_app\assets\{f.name}"        
            with open(path, 'wb') as FH:
                for chunk in f.chunks():
                    FH.write(chunk)        

        return render(request=request, template_name='my_app/base.html',        
                    context= {'message': 'הטופס התקבל בהצלחה'})


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
