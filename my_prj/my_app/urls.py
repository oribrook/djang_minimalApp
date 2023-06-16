from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        
    path('car_list', views.car_list, name='car_list'),        
    path('car/<int:id>', views.car, name='car'),
    path('car/search', views.search_car, name='search_car'),
    path('contact_as', views.ContactView.as_view(), name='contact'),
    path('car/add', views.add_car, name='add_car'),
    path('car/edit/<int:id_>', views.edit_car, name='edit_car'),
    path('user_cars', views.user_cars, name='user_cars'),
    path('test', views.CarCreateView.as_view(), name='test'),
    path('user/signup', views.carbnb_signup, name='signup'),
    path('user/login', views.carbnb_login, name='login'),
    path('private', views.private, name='private'),
]
