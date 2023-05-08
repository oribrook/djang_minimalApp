from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup),
    path('private', views.private),
    path('obtain-token', obtain_auth_token),
    path('check-token', views.check_token),
]
