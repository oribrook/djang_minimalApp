from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.views import View
from .models import Car
from django.db.transaction import atomic
from .forms import ContactForm, CarForm
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic import CreateView


class CarCreateView(CreateView):
    model = Car
    fields = "__all__"
    template_name = "my_app/form.html"
    context_object_name = 'form'
    success_url = '/'

    def get_context_data(self, *args, **keyword):
        context = super().get_context_data(*args, **keyword)
        context['url'] = reverse('test')
        return context

class CarListView(ListView):
    model = Car
    # queryset = Car.objects.filter(cost__gt=500)
    context_object_name = 'cars'
    template_name = 'my_app/cars_list.html'



@require_http_methods(["GET", "POST"])
def edit_car(request, id_):
    car = get_object_or_404(Car, id=id_)

    form = CarForm(instance=car, is_year_editable=True)
    form.fields['car_type'].disabled = True
    if request.method == 'GET':
        return render(request=request, template_name='my_app/form.html',
                      context={'form': form,
                               'url': reverse('edit_car', kwargs={'id_': id_})})

    else:
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            print("Valid")
            form.save()
            return render(request=request, template_name='my_app/base.html',
                      context={'message': 'המכונית התעדכנה',})

        print("Not Valid")
        print(form.errors)
        return render(request=request, template_name='my_app/form.html',
                      context={'form': form,
                               'url': reverse('edit_car', kwargs={'id_': id_})})

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

@require_http_methods(["GET", ])
def user_cars(request):
    user_id = 1
    cars = Car.objects.filter(owner=user_id)

    return render(request=request, template_name='my_app/cars_list.html',
                  context={'cars': cars, 'to_edit': True})

