import IPython
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.views import View
from .models import Car, Person
from django.db.transaction import atomic
from .forms import (ContactForm, CarForm, LoginForm, MyUserCreationForm,
                    MyUserUpdateForm)
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import  login_required
import IPython

def private(request):

    if request.user.is_authenticated:
        return render(request=request, template_name='my_app/base.html',
                      context={'message': ' זהו מידע חסוי שנגיש לך כי אתה מחובר'})

    return render(request=request, template_name='my_app/base.html',
                      context={'message': 'אין לך הרשאה כי אתה לא מחובר. התחבר תחילה'})


@require_http_methods(["GET", "POST"])
def carbnb_login(request):
    if request.method == 'GET':
        return render(request=request, template_name="my_app/form.html",
                      context={
                          'form': LoginForm,
                          'url': reverse("login"),
                      })

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return render(request=request, template_name='my_app/base.html',
                      context={'message': 'התחברת בהצלחה'})

    return render(request=request, template_name="my_app/form.html",
                  context={
                      'form': LoginForm,
                      'url': reverse("login"),
                      'message': 'ההתחברות נכשלה נסה שנית',
                  })

@require_http_methods(["GET", "POST"])
def carbnb_signup(request):
    if request.method == 'GET':
        return render(request=request, template_name='my_app/form.html',
                      context={'url': reverse('signup'),
                            #    'form': UserCreationForm()
                               'form': MyUserCreationForm()
                               })

    # form = UserCreationForm(request.POST)
    form = MyUserCreationForm(request.POST)
    if not form.is_valid():
        return render(request=request, template_name='my_app/form.html',
                      context={'url': reverse('signup'),
                               'form': form})
    # else (form valid)
    user = form.save()
    login(request=request, user=user)
    Person.objects.create(name=user.username, 
                          address=form.cleaned_data['address'],
                          user=user,
                          person_id=form.cleaned_data['person_id'])
    
    return render(request=request, template_name='my_app/base.html',
                  context={'message': 'ברוך הבא לאתר שלנו'})


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

    form = CarForm(instance=car)
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

@login_required
@require_http_methods(["GET", ])
def user_cars(request):

    person = Person.objects.get(user=request.user)
    cars = Car.objects.filter(owner=person)

    return render(request=request, template_name='my_app/cars_list.html',
                  context={'cars': cars, 'to_edit': True})


def carbnb_logout(request):    
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


@login_required
def update_user_info(request):
    form = MyUserUpdateForm(instance=request.user)
    # del form.fields['password1']
    # del form.fields['password2']
    if request.method == 'GET':
        return render(request=request, template_name='my_app/form.html',
                        context={'form': form,
                                 'url': reverse('update_user')})
    
    if request.method == 'POST':
        form = MyUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        
        return render(request=request, template_name='my_app/base.html',        
                    context= {'message': 'הנתונים התעדכנו'})