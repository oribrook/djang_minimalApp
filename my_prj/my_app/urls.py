from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('file', views.save_file, name='file'),
]
