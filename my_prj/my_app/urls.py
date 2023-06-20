from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

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
    # path('user/login', views.carbnb_login, name='login'),
    path('user/login', LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='my_app/form.html',
            # extra_context={'url': 'login'}
            ), 
        name='login'),
    
    # path('user/logout', views.carbnb_logout, name='logout'),
    path('user/logout', LogoutView.as_view(next_page='home'), name='logout'),
    path('user/update', views.update_user_info, name='update_user'),
    path('private', views.private, name='private'),
]
