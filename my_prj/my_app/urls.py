from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home),
    path('html', views.serve_html, name='html'),
    path('param/<str:param>', views.serve_param, name='param'),
    path('extended', views.serve_extended_html, name='extended'),
] 
