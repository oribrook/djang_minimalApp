from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        
    path('car_list', views.car_list, name='car_list'),        
    path('car/<int:id>', views.car, name='car'),
    path('car/search', views.search_car, name='search_car'),
    path('contact_as', views.ContactView.as_view(), name='contact'),
    path('car/add', views.add_car, name='add_car'),    
]
